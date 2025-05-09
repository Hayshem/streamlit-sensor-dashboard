import os
import json
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from datetime import datetime
from prophet import Prophet
from prophet.plot import plot_plotly
from google.oauth2.service_account import Credentials
import io
import pandas as pd  # Make sure you import pandas

# Get credentials from Streamlit secrets
credentials_dict = st.secrets["GOOGLE_CREDENTIALS"]

# Convert the secret dictionary to a Credentials object
credentials = Credentials.from_service_account_info(credentials_dict, scopes=["https://www.googleapis.com/auth/drive.readonly"])

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Folder ID and file name
SPREADSHEET_ID = '11FHOapzFiKa0iim6evuCLcbsBZEp0j3-'
SHEET_NAME = 'SensorData'

@st.cache
def fetch_sheet_as_df(spreadsheet_id: str, sheet_name: str) -> pd.DataFrame:
    # build the Sheets API client
    sheets = build("sheets", "v4", credentials=credentials).spreadsheets()

    # pull every row/column of that sheet tab
    result = sheets.values().get(
        spreadsheetId=spreadsheet_id,
        range=sheet_name
    ).execute()

    values = result.get("values", [])
    if not values or len(values) < 2:
        st.error(f"No data found in sheet '{sheet_name}'.")
        return pd.DataFrame()

    # first row is header, rest is data
    header, *rows = values
    return pd.DataFrame(rows, columns=header)

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


if data is not None:
    # Show the latest data
    st.write("### Current Data", data.tail())

    # Visualizations
    st.write("### Data Visualization")
    for column in ['Temperature', 'Humidity', 'Air Quality', 'Electricity Usage']:
        st.line_chart(data[column])

    # Forecasting
    st.write("### Forecast for the Next 24 Hours")
    column_to_forecast = st.selectbox("Select Parameter to Forecast", ['Temperature', 'Humidity', 'Air Quality', 'Electricity Usage'])
    forecast_data, model = forecast(data, column_to_forecast)
    forecast_fig = plot_plotly(model, forecast_data)
    st.plotly_chart(forecast_fig)

    # Notifications
    st.write("### Insights and Notifications")
    if column_to_forecast == 'Electricity Usage' and forecast_data['yhat'].iloc[-1] > 50:
        st.warning("High electricity consumption forecasted!")
else:
    st.error("Unable to fetch the CSV file. Please check the folder ID or file name.")

