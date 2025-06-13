import streamlit as st

# Inject custom CSS
st.markdown("""
<style>
/* Center the button container */
.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px; /* Spacing between buttons */
    margin-top: 50px;
}

/* Style individual buttons */
div.stButton > button {
    height: 100px;
    width: 200px;
    font-size: 18px;
    border-radius: 10px;
    border: none;
    color: white;
    cursor: pointer;
    font-weight: bold;
}

/* Button colors */
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
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
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
    st.markdown("</div>", unsafe_allow_html=True)

# Outdoor Page
def outdoor_page():
    st.write("### Outdoor Environmental Data")
    st.markdown("[Go to Outdoor Information Resource](https://meteo.it)")
    if st.button("Back", key="back_outdoor"):
        st.session_state.page = "main"

# Indoor Page
def indoor_page():
    st.write("### Indoor Environmental Data")
    st.markdown("[Go to Indoor Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.markdown("[Go to Indoor Dashboard 2](https://telefragmont-node2.streamlit.app/)")
    st.markdown("[Go to Indoor Dashboard 3](https://telefragmont-node3.streamlit.app/)")
    if st.button("Back", key="back_indoor"):
        st.session_state.page = "main"

# Medical Page
def medical_page():
    st.write("### Medical Data")
    st.markdown("[Go to Medical Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    if st.button("Back", key="back_medical"):
        st.session_state.page = "main"

# Social Page
def social_page():
    st.write("### Social Data")
    st.markdown("[Go to Social Resource 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.markdown("[Go to Social Resource 2](https://torino.circololettori.it/gruppi-25-2/)")
    st.markdown("[Go to Social Resource 3](https://www.compagniadeimeglioinsieme.com/i-gruppi/gruppo-camminiamoinsieme-fitel-piemonte/)")
    st.markdown("[Go to Social Resource 4](https://www.promozionedellasalute.it/iniziative/comunita/gruppi-di-cammino)")
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
