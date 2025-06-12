import streamlit as st

# App Title
st.title("Environmental Data Dashboard")

st.markdown("### Select a Category:")

# Buttons for different categories
col1, col2 = st.columns(2)

with col1:
    if st.button("Outdoor Environmental Data"):
        st.write("Redirecting...")
        st.markdown("[Go to Outdoor Data Dashboard](https://meteo.it)")

    if st.button("Medical Data"):
        st.write("Redirecting...")
        st.markdown("[Go to Medical Data Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")

with col2:
    if st.button("Indoor Environmental Data"):
        st.write("Redirecting...")
        st.markdown("[Go to Indoor Data Dashboard](https://telefragmont-node1.streamlit.app/)")

    if st.button("Social Data"):
        st.write("Redirecting...")
        st.markdown("[Go to Social Data Dashboard](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")

# Footer
st.markdown("---")
st.caption("Designed for ease of use. Click a button to access the respective data dashboard.")

