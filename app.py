import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from datetime import datetime
from prophet import Prophet
from prophet.plot import plot_plotly
from google.oauth2.service_account import Credentials
import io

# Path to your credentials.json file
SERVICE_ACCOUNT_FILE = r"C:\Users\Hayshem Ali Butt\Desktop\Nodes\credentials.json"
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Folder ID and file name
FOLDER_ID = '11FHOapzFiKa0iim6evuCLcbsBZEp0j3-'
FILE_NAME = 'sensor_data.csv'

# Function to fetch CSV from Google Drive folder
@st.cache
def fetch_csv_from_folder(folder_id, file_name):
    # Authenticate using the service account
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    # Search for the file by name in the specified folder
    query = f"'{folder_id}' in parents and name='{file_name}' and mimeType='text/csv'"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    files = results.get('files', [])

    if not files:
        st.error("CSV file not found in the specified folder.")
        return None

    # Fetch the file's ID
    file_id = files[0]['id']

    # Download the file content
    request = service.files().get_media(fileId=file_id)
    file_data = io.BytesIO()
    downloader = MediaIoBaseDownload(file_data, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    file_data.seek(0)
    return pd.read_csv(file_data)

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
data = fetch_csv_from_folder(FOLDER_ID, FILE_NAME)

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

