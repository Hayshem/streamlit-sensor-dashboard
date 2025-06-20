import streamlit as st

# Inject custom CSS for button styling
st.markdown("""
    <style>
        div.stButton > button {
            height: 100px; /* Set button height */
            width: 200px; /* Set button width */
            font-size: 16px; /* Font size for button text */
            margin: 10px; /* Space between buttons */
            border-radius: 8px; /* Rounded corners */
            border: none; /* Remove border */
            color: white; /* Text color */
            cursor: pointer; /* Pointer cursor */
        }
        /* Unique button colors */
        div.stButton > button.outdoor { background-color: #3498db; } /* Blue */
        div.stButton > button.indoor { background-color: #2ecc71; } /* Green */
        div.stButton > button.medical { background-color: #f39c12; } /* Orange */
        div.stButton > button.social { background-color: #e74c3c; } /* Red */

        /* Hover effects */
        div.stButton > button.outdoor:hover { background-color: #2980b9; }
        div.stButton > button.indoor:hover { background-color: #27ae60; }
        div.stButton > button.medical:hover { background-color: #d35400; }
        div.stButton > button.social:hover { background-color: #c0392b; }
    </style>
""", unsafe_allow_html=True)

# Main page
def main_page():
    st.title("Main Dashboard")
    st.write("Choose an option:")

    # Arrange buttons in two columns
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Outdoor Environmental Data", key="outdoor", help="Outdoor Environmental Data"):
            st.session_state.page = "outdoor"

        if st.button("Indoor Environmental Data", key="indoor", help="Indoor Environmental Data"):
            st.session_state.page = "indoor"

    with col2:
        if st.button("Medical Data", key="medical", help="Medical Data"):
            st.session_state.page = "medical"

        if st.button("Social Data", key="social", help="Social Data"):
            st.session_state.page = "social"

# Outdoor Page
def outdoor_page():
    st.title("Outdoor Environmental Data")
    st.write("[Go to Outdoor Information Resource](https://meteo.it)")
    if st.button("Back"):
        st.session_state.page = "main"

# Indoor Page
def indoor_page():
    st.title("Indoor Environmental Data")
    st.write("[Go to Indoor Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.write("[Go to Indoor Dashboard 2](https://telefragmont-node2.streamlit.app/)")
    st.write("[Go to Indoor Dashboard 3](https://telefragmont-node3.streamlit.app/)")
    if st.button("Back"):
        st.session_state.page = "main"

# Medical Page
def medical_page():
    st.title("Medical Data")
    st.write("[Go to Medical Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    if st.button("Back"):
        st.session_state.page = "main"

# Social Page
def social_page():
    st.title("Social Data")
    st.write("[Go to Social Resource 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.write("[Go to Social Resource 2](https://torino.circololettori.it/gruppi-25-2/)")
    st.write("[Go to Social Resource 3](https://www.compagniadeimeglioinsieme.com/i-gruppi/gruppo-camminiamoinsieme-fitel-piemonte/)")
    st.write("[Go to Social Resource 4](https://www.promozionedellasalute.it/iniziative/comunita/gruppi-di-cammino)")
    if st.button("Back"):
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
