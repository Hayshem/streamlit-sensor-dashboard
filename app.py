import os
import json
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from datetime import datetime
from prophet import Prophet
from google.oauth2.service_account import Credentials
import io
import pandas as pd
import plotly.graph_objects as go


# Get credentials from Streamlit secrets
credentials_dict = st.secrets["GOOGLE_CREDENTIALS"]

# Convert the secret dictionary to a Credentials object
credentials = Credentials.from_service_account_info(credentials_dict, scopes=["https://www.googleapis.com/auth/drive.readonly"])

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/spreadsheets.readonly"
]

# Folder ID and file name
SPREADSHEET_ID = '1L-f5sLjb0Gt_6ZWQizS-tCCINkTg59jKZaLdj4Nr2ys'
SHEET_NAME = 'Sheet1'

@st.cache
def fetch_sheet_as_df(spreadsheet_id: str, sheet_name: str) -> pd.DataFrame:
    try:
        # Build the Sheets API client
        sheets = build("sheets", "v4", credentials=credentials).spreadsheets()

        # Pull data from the specified sheet tab
        result = sheets.values().get(
            spreadsheetId=spreadsheet_id,
            range=sheet_name
        ).execute()

        values = result.get("values", [])
        if not values or len(values) < 2:
            st.warning(f"No data found in sheet '{sheet_name}'. Ensure the sheet has a header row and data.")
            return pd.DataFrame()

        # First row is header, remaining rows are data
        header, *rows = values
        return pd.DataFrame(rows, columns=header)

    except Exception as e:
        st.error(f"Error fetching data from Google Sheets: {str(e)}")
        return pd.DataFrame()

# Forecasting function
def forecast(data, column, periods=24):
    df = data[['Timestamp', column]].copy()
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'])
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods, freq='H')
    forecast = model.predict(future)
    return forecast, model

# Streamlit Dashboard
st.title("Real-Time Sensor Data Dashboard")

# Fetch real-time data from Google Drive
data = fetch_sheet_as_df(SPREADSHEET_ID, SHEET_NAME)

# Clean column names
if not data.empty:
    data.columns = data.columns.str.strip()

    # Show the latest data
    st.write("### Current Data", data.tail())

    # Visualizations
    st.write("### Data Visualization")
    for column in ['Temperature', 'Humidity', 'Air Quality', 'Electricity Usage']:
        if column in data.columns:
            st.line_chart(data[column])
        else:
            st.warning(f"Column '{column}' is not present in the data.")
    

    # Forecasting function
    def forecast(data, column, periods=24):
        df = data[['Timestamp', column]].copy()
        df.columns = ['ds', 'y']
        df['ds'] = pd.to_datetime(df['ds'])
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=periods, freq='H')
        forecast = model.predict(future)
        return forecast, model

    # Plot forecast function
    def plot_forecast(forecast_data, parameter):
        fig = go.Figure()

        # Add actual values
        fig.add_trace(go.Scatter(
            x=forecast_data['ds'],
            y=forecast_data['yhat'],
            mode='lines',
            name=f'Forecasted {parameter}'
        ))

        # Add uncertainty intervals
        fig.add_trace(go.Scatter(
            x=forecast_data['ds'],
            y=forecast_data['yhat_upper'],
            mode='lines',
            line=dict(width=0),
            name='Upper Confidence Interval',
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=forecast_data['ds'],
            y=forecast_data['yhat_lower'],
            mode='lines',
            line=dict(width=0),
            name='Lower Confidence Interval',
            showlegend=False,
            fill='tonexty',
            fillcolor='rgba(0,100,250,0.2)'
        ))

        # Customize layout
        fig.update_layout(
            title=f'{parameter} Forecast',
            xaxis_title='Timestamp',
            yaxis_title=parameter,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        return fig


    # Forecasting
    st.write("### Forecast for the Next 24 Hours")
    column_to_forecast = st.selectbox("Select Parameter to Forecast", ['Temperature', 'Humidity', 'Air Quality', 'Electricity Usage'])

    if column_to_forecast in data.columns:
        try:
            # Perform forecasting
            forecast_data, model = forecast(data, column_to_forecast)

            # Visualize the forecast using the custom plot function
            forecast_fig = plot_forecast(forecast_data, column_to_forecast)
            st.plotly_chart(forecast_fig)

            # Notifications
            st.write("### Insights and Notifications")
            latest_forecast_value = forecast_data['yhat'].iloc[-1]

            if column_to_forecast == 'Electricity Usage' and latest_forecast_value > 50:
                st.warning("High electricity consumption forecasted!")
            elif column_to_forecast == 'Temperature':
                if latest_forecast_value < 18:
                    st.warning("Low temperature forecasted! Take precautions against cold.")
                elif latest_forecast_value > 29.4:
                    st.warning("High temperature forecasted! Take precautions against heat.")
            elif column_to_forecast == 'Humidity':
                if latest_forecast_value < 25:
                    st.warning("Low humidity forecasted! Take precautions to stay hydrated.")
                elif latest_forecast_value > 70:
                    st.warning("High humidity forecasted! Take precautions against discomfort.")
            elif column_to_forecast == 'Air Quality':
                if latest_forecast_value > 100:
                    if latest_forecast_value <= 150:
                        st.warning("Air Quality Index indicates 'Unhealthy for Sensitive Groups'. Take precautions.")
                    elif latest_forecast_value <= 200:
                        st.warning("Air Quality Index indicates 'Unhealthy'. Take precautions.")
                    elif latest_forecast_value <= 300:
                        st.warning("Air Quality Index indicates 'Very Unhealthy'. Limit exposure and take precautions.")
                    else:
                        st.warning("Air Quality Index indicates 'Hazardous'. Stay indoors and take precautions.")

        except Exception as e:
            st.error(f"Error during forecasting: {e}")
    else:
        st.error(f"Column '{column_to_forecast}' is not present in the data.")