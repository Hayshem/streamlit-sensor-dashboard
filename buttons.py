import streamlit as st

st.markdown("""
<style>
div.stButton > button {
    height: 100px; /* Adjust height for larger buttons */
    width: 150px;  /* Adjust width for square buttons */
    font-size: 20px; /* Adjust font size */
    margin: 10px;  /* Add space between buttons */
    color: white;  /* Button text color */
    border-radius: 15px; /* Rounded corners */
}
div.stButton > button:first-of-type { background-color: #3498db; } /* Blue */
div.stButton > button:nth-of-type(2) { background-color: #2ecc71; } /* Green */
div.stButton > button:nth-of-type(3) { background-color: #f39c12; } /* Orange */
div.stButton > button:nth-of-type(4) { background-color: #e74c3c; } /* Red */
</style>
""", unsafe_allow_html=True)

# Main page
def main_page():
    # Create a grid layout for buttons
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Outdoor Environmental Data Button
        if st.button("Outdoor Environmental Data",  key="outdoor"):
            st.session_state.page = "outdoor"

        # Indoor Environmental Data Button
        if st.button("Indoor Environmental Data",  key="indoor"):
            st.session_state.page = "indoor"

    with col2:
        # Medical Data Button
        if st.button("Medical Data", key="medical"):
            st.session_state.page = "medical"

        # Social Data Button
        if st.button("Social Data", key="social"):
            st.session_state.page = "social"

# Outdoor Page
def outdoor_page():
    st.write("### Outdoor Environmental Data")
    st.markdown("[Go to Outdoor Information Resource](https://meteo.it)")
    st.button("Back", on_click=lambda: setattr(st.session_state, "page", "main"))

# Indoor Page
def indoor_page():
    st.write("### Indoor Environmental Data")
    st.markdown("[Go to Indoor Information Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.markdown("[Go to Indoor Information Dashboard 2](https://telefragmont-node2.streamlit.app/)")
    st.markdown("[Go to Indoor Information Dashboard 3](https://telefragmont-node3.streamlit.app/)")
    st.button("Back", on_click=lambda: setattr(st.session_state, "page", "main"))

# Medical Page
def medical_page():
    st.write("### Medical Data")
    st.markdown("[Go to Medical Data Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    st.button("Back", on_click=lambda: setattr(st.session_state, "page", "main"))

# Social Page
def social_page():
    st.write("### Social Data")
    st.markdown("[Go to Social Information Resource 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.markdown("[Go to Social Information Resource 2](https://torino.circololettori.it/gruppi-25-2/)")
    st.markdown("[Go to Social Information Resource 3](https://www.compagniadeimeglioinsieme.com/i-gruppi/gruppo-camminiamoinsieme-fitel-piemonte/)")
    st.markdown("[Go to Social Information Resource 4](https://www.promozionedellasalute.it/iniziative/comunita/gruppi-di-cammino)")
    st.button("Back", on_click=lambda: setattr(st.session_state, "page", "main"))

# Routing based on the selected page
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
