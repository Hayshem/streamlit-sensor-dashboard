import os
import json
#from socket import errorTab
import socket
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from datetime import datetime
from prophet import Prophet
from prophet.plot import plot_plotly
from google.oauth2.service_account import Credentials
import io
import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
from PIL import Image

# Load the logo images
logo1 = Image.open("images.png")  # First logo path
logo2 = Image.open("NODES_Logo.png")  # Second logo path

# A layout with two columns for logos
col1, col2 = st.columns(2)

# Display logos in the respective columns
with col1:
    st.image(logo1, use_column_width=True)

with col2:
    st.image(logo2, use_column_width=True)

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

@st.cache_data(ttl=300)
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
st.title("Cruscotto in Tempo Reale delle Metriche Ambientali")

# Fetch real-time data from Google Drive
data = fetch_sheet_as_df(SPREADSHEET_ID, SHEET_NAME)

# Clean column names
if not data.empty:
    data.columns = data.columns.str.strip()

    # Show the latest data
    st.write("### Dati Attuali", data.tail())

    # Mapping of column names from English to Italian
    column_translation = {
    'Temperature': 'Temperatura',
    'Humidity': 'Umidita',
    'Air Quality': 'Qualita dell\'aria',
    'Electricity Usage': 'Consumo di elettricita'
    }

    # Visualizations
    st.write("### Visualizzazione dei Dati")
    missing_columns = []  # To track missing columns

    # Ensure Timestamp column is present and properly formatted
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])  # Convert to datetime if not already
       # data.set_index('Timestamp', inplace=True)  # Set as index for proper plotting

    for column in ['Temperature', 'Humidity', 'Air Quality', 'Electricity Usage']:
        if column in data.columns:
            italian_column_name = column_translation.get(column, column)  # Get Italian name or fallback to original


            fig = px.line(
                data_frame=data,
                x='Timestamp',
                y=column,
                title=f"Andamento di {italian_column_name}",
                labels={"Timestamp": "Tempo", column: italian_column_name},
            )
            st.plotly_chart(fig)
            #st.write(f"#### Andamento di {italian_column_name}")
            #st.line_chart(data[column])
        else:
            missing_columns.append(column_translation.get(column, column))
    if missing_columns:
        st.warning(f"Colonne mancanti nei dati: {', '.join(missing_columns)}")

             #original_name = column_translation.get(column, column)
             #st.warning(f"Colonna '{column_translation.get(column, column)}' non presente nei dati.")


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
        italian_label = parameter_translation.get(parameter, parameter)  # Translate parameter name to Italian
    
        fig = go.Figure()

        # Add actual values (forecasted values)
        fig.add_trace(go.Scatter(
            x=forecast_data['ds'],
            y=forecast_data['yhat'],
            mode='lines',
            name=f"Previsione di {italian_label}"  # Forecasted label in Italian
        ))

        # Add uncertainty intervals (upper confidence)
        fig.add_trace(go.Scatter(
            x=forecast_data['ds'],
            y=forecast_data['yhat_upper'],
            mode='lines',
            line=dict(width=0),
            name="Intervallo di confidenza superiore",  # Upper confidence interval in Italian
            showlegend=False
        ))

        # Add uncertainty intervals (lower confidence)
        fig.add_trace(go.Scatter(
            x=forecast_data['ds'],
            y=forecast_data['yhat_lower'],
            mode='lines',
            line=dict(width=0),
            name="Intervallo di confidenza inferiore",  # Lower confidence interval in Italian
            showlegend=False,
            fill='tonexty',
            fillcolor='rgba(0,100,250,0.2)'
        ))

        # Customize layout with Italian labels
        fig.update_layout(
            title=f"Previsione di {italian_label}",  # Title in Italian
            xaxis_title="Tempo",  # x-axis label in Italian
            yaxis_title=italian_label,  # y-axis label in Italian
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        )

        return fig



    # Forecasting
    st.write("### Previsioni per le Prossime 24 Ore")
    #column_to_forecast = st.selectbox("Seleziona il parametro da prevedere", ['Temperature', 'Humidity', 'Air Quality', 'Electricity Usage'])
    # Mapping of parameters from English to Italian
    parameter_translation = {
    'Temperature': 'Temperatura',
    'Humidity': 'Umidita',
    'Air Quality': 'Qualita dell\'aria',
    'Electricity Usage': 'Consumo di elettricita'
    }

    # Reverse mapping for processing
    reverse_translation = {v: k for k, v in parameter_translation.items()}

    # Display selection box in Italian
    column_to_forecast_italian = st.selectbox(
        "Seleziona il parametro da prevedere",
        list(parameter_translation.values())
    )

    # Map the selected Italian parameter back to English for processing
    #column_to_forecast = reverse_translation[column_to_forecast_italian]
    column_to_forecast = reverse_translation.get(column_to_forecast_italian)

    if column_to_forecast in data.columns:
        try:
            # Perform forecasting
            forecast_data, model = forecast(data, column_to_forecast)

            # Visualize the forecast using the custom plot function
            forecast_fig = plot_forecast(forecast_data, column_to_forecast)
            st.plotly_chart(forecast_fig)

            # Notifications
            st.write("### Previsione e Notifiche")
            latest_forecast_value = forecast_data['yhat'].iloc[-1]

            if column_to_forecast == 'Electricity Usage' and latest_forecast_value > 50:
                st.write(f"Valore previsto della consumo di elettricita: {latest_forecast_value}")
                st.warning("Previsione di un alto consumo di elettricita!")
            elif column_to_forecast == 'Temperature':
                st.write(f"Valore previsto della temperatura: {latest_forecast_value}")
                if latest_forecast_value < 18:
                    st.warning("Previsione di bassa temperatura! Prendere precauzioni contro il freddo.")
                elif 18 <= latest_forecast_value <= 29.4:
                    st.success("I valori della temperatura sono normali.")
                elif latest_forecast_value > 29.4:
                    st.warning("Previsione di alta temperatura! Prendere precauzioni contro il caldo.")
            elif column_to_forecast == 'Humidity':
                st.write(f"Valore previsto dell'umidita: {latest_forecast_value}")
                if latest_forecast_value < 25:
                    st.warning("Bassa umidita prevista! Prendere precauzioni per rimanere idratati.")
                elif 25 <= latest_forecast_value <= 70:
                    st.success("I valori di umidita sono normali.")
                elif latest_forecast_value > 70:
                     st.warning("Previsione di alta umidita! Prendere precauzioni contro il disagio.")

            elif column_to_forecast == 'Air Quality':
                st.write(f"Valore previsto della qualita dell'aria: {latest_forecast_value}")
                if latest_forecast_value < 100:
                    st.success("I valori della qualita dell'aria sono normali.")
                elif 100 <= latest_forecast_value <= 150:
                    st.warning("L'indice della qualita dell'aria indica 'Non salutare per le persone sensibili'. Prendere precauzioni.")
                elif 150 < latest_forecast_value <= 200:
                    st.warning("L'indice della qualita dell'aria indica 'Non salutare'. Prendere precauzioni.")
                elif 200 < latest_forecast_value <= 300:
                    st.warning("L'indice della qualita dell'aria indica 'Non molto salutare'. Limitare l'esposizione e prendere precauzioni.")
                else:
                    st.warning("L'indice della qualita dell'aria indica 'Pericoloso'. Rimani al chiuso e prendi precauzioni.")

        except Exception as e:
            st.error(f"Error during forecasting: {e}")
    else:
        st.error(f"Column '{column_to_forecast}' is not present in the data.")
