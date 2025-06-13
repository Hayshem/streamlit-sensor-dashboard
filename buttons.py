import streamlit as st

# Inject custom CSS
st.markdown("""
<style>
/* Centering buttons */
div.full-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Full viewport height */
    padding: 0;
    margin: 0;
    flex-wrap: wrap; /* Allow wrapping if necessary */
}

/* Button styles */
button.custom-button {
    height: 100px; /* Button height */
    width: 200px; /* Button width */
    font-size: 18px; /* Font size */
    border-radius: 10px; /* Rounded corners */
    margin: 10px; /* Space between buttons */
    border: none; /* Remove border */
    cursor: pointer; /* Pointer cursor */
    color: white; /* Text color */
}

/* Button colors */
button.outdoor {
    background-color: #3498db; /* Blue */
}
button.indoor {
    background-color: #2ecc71; /* Green */
}
button.medical {
    background-color: #f39c12; /* Orange */
}
button.social {
    background-color: #e74c3c; /* Red */
}

/* Hover states */
button.outdoor:hover {
    background-color: #2980b9;
}
button.indoor:hover {
    background-color: #27ae60;
}
button.medical:hover {
    background-color: #d35400;
}
button.social:hover {
    background-color: #c0392b;
}

/* Back button styles */
button.back-button {
    height: 50px; /* Smaller height */
    width: 120px; /* Smaller width */
    font-size: 16px; /* Smaller font size */
    background-color: #555; /* Dark gray */
    color: white; /* Text color */
    border-radius: 5px; /* Rounded corners */
    margin: 10px; /* Space between buttons */
    border: none; /* Remove border */
    cursor: pointer; /* Pointer cursor */
}
button.back-button:hover {
    background-color: #333; /* Darker gray */
}
</style>
""", unsafe_allow_html=True)

# Main page
def main_page():
    st.markdown("<div class='full-page'>", unsafe_allow_html=True)
    if st.button("Outdoor Environmental Data", key="outdoor", help="Click to view outdoor data"):
        st.session_state.page = "outdoor"
    if st.button("Indoor Environmental Data", key="indoor", help="Click to view indoor data"):
        st.session_state.page = "indoor"
    if st.button("Medical Data", key="medical", help="Click to view medical data"):
        st.session_state.page = "medical"
    if st.button("Social Data", key="social", help="Click to view social data"):
        st.session_state.page = "social"
    st.markdown("</div>", unsafe_allow_html=True)

# Outdoor Page
def outdoor_page():
    st.write("### Outdoor Environmental Data")
    st.markdown("[Go to Outdoor Information Resource](https://meteo.it)")
    if st.button("Back", key="back_outdoor", use_container_width=True):
        st.session_state.page = "main"

# Indoor Page
def indoor_page():
    st.write("### Indoor Environmental Data")
    st.markdown("[Go to Indoor Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.markdown("[Go to Indoor Dashboard 2](https://telefragmont-node2.streamlit.app/)")
    st.markdown("[Go to Indoor Dashboard 3](https://telefragmont-node3.streamlit.app/)")
    if st.button("Back", key="back_indoor", use_container_width=True):
        st.session_state.page = "main"

# Medical Page
def medical_page():
    st.write("### Medical Data")
    st.markdown("[Go to Medical Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    if st.button("Back", key="back_medical", use_container_width=True):
        st.session_state.page = "main"

# Social Page
def social_page():
    st.write("### Social Data")
    st.markdown("[Go to Social Resource 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.markdown("[Go to Social Resource 2](https://torino.circololettori.it/gruppi-25-2/)")
    st.markdown("[Go to Social Resource 3](https://www.compagniadeimeglioinsieme.com/i-gruppi/gruppo-camminiamoinsieme-fitel-piemonte/)")
    st.markdown("[Go to Social Resource 4](https://www.promozionedellasalute.it/iniziative/comunita/gruppi-di-cammino)")
    if st.button("Back", key="back_social", use_container_width=True):
        st.session_state.page = "main"

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
