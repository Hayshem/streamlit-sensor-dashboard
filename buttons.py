import streamlit as st

# Main page
def main_page():
    st.title("Main Dashboard")
    st.write("Choose an option:")

    # Arrange buttons in two columns
    col1, col2 = st.columns(2, gap="large")
    with col1:
        if st.button("Outdoor Environmental Data", key="outdoor"):
            st.session_state.page = "outdoor"

        if st.button("Indoor Environmental Data", key="indoor"):
            st.session_state.page = "indoor"

    with col2:
        if st.button("Medical Data", key="medical"):
            st.session_state.page = "medical"

        if st.button("Social Data", key="social"):
            st.session_state.page = "social"

# Outdoor Page
def outdoor_page():
    st.title("Outdoor Environmental Data")
    st.write("[Go to Outdoor Information Resource](https://meteo.it)")
    if st.button("Back", key="back_outdoor"):
        st.session_state.page = "main"

# Indoor Page
def indoor_page():
    st.title("Indoor Environmental Data")
    st.write("[Go to Indoor Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.write("[Go to Indoor Dashboard 2](https://telefragmont-node2.streamlit.app/)")
    st.write("[Go to Indoor Dashboard 3](https://telefragmont-node3.streamlit.app/)")
    if st.button("Back", key="back_indoor"):
        st.session_state.page = "main"

# Medical Page
def medical_page():
    st.title("Medical Data")
    st.write("[Go to Medical Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    if st.button("Back", key="back_medical"):
        st.session_state.page = "main"

# Social Page
def social_page():
    st.title("Social Data")
    st.write("[Go to Social Resource 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.write("[Go to Social Resource 2](https://torino.circololettori.it/gruppi-25-2/)")
    st.write("[Go to Social Resource 3](https://www.compagniadeimeglioinsieme.com/i-gruppi/gruppo-camminiamoinsieme-fitel-piemonte/)")
    st.write("[Go to Social Resource 4](https://www.promozionedellasalute.it/iniziative/comunita/gruppi-di-cammino)")
    if st.button("Back", key="back_social"):
        st.session_state.page = "main"

# Routing logic
if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "outdoor":
    outdoor_page()
elif st.session_state.page == "indoor":
    indoor_page()
elif st.session_state.page == "medical":
    medical_page()
elif st.session_state.page == "social":
    social_page()
