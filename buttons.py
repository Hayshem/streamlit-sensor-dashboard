import streamlit as st

# Inject custom CSS
st.markdown("""
<style>
/* Center all content vertically and horizontally */
main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    padding: 0;
    margin: 0;
}

/* Style for main buttons */
div.stButton > button {
    height: 100px; /* Height for larger buttons */
    width: 150px; /* Width for square buttons */
    font-size: 18px; /* Adjust font size */
    margin: 10px; /* Space between buttons */
    color: white; /* Text color */
    border-radius: 15px; /* Rounded corners */
}

/* Colors for each button */
div.stButton > button:first-of-type { background-color: #3498db; } /* Blue */
div.stButton > button:nth-of-type(2) { background-color: #2ecc71; } /* Green */
div.stButton > button:nth-of-type(3) { background-color: #f39c12; } /* Orange */
div.stButton > button:nth-of-type(4) { background-color: #e74c3c; } /* Red */

/* Style for the smaller back button */
.back-button button {
    height: 40px; /* Smaller height */
    width: 80px; /* Smaller width */
    font-size: 14px; /* Smaller font size */
    background-color: #555; /* Dark gray background */
    color: white; /* White text */
    border-radius: 10px; /* Rounded corners */
}
</style>
""", unsafe_allow_html=True)

# Main page
def main_page():
    # Display buttons in the center
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
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
    
    st.markdown("</div>", unsafe_allow_html=True)

# Outdoor Page
def outdoor_page():
    st.write("### Outdoor Environmental Data")
    st.markdown("[Go to Outdoor Information Resource](https://meteo.it)")
    st.markdown('<div class="back-button" style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Back", key="back_outdoor"):
        st.session_state.page = "main"
    st.markdown('</div>', unsafe_allow_html=True)

# Indoor Page
def indoor_page():
    st.write("### Indoor Environmental Data")
    st.markdown("[Go to Indoor Information Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.markdown("[Go to Indoor Information Dashboard 2](https://telefragmont-node2.streamlit.app/)")
    st.markdown("[Go to Indoor Information Dashboard 3](https://telefragmont-node3.streamlit.app/)")
    st.markdown('<div class="back-button" style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Back", key="back_indoor"):
        st.session_state.page = "main"
    st.markdown('</div>', unsafe_allow_html=True)

# Medical Page
def medical_page():
    st.write("### Medical Data")
    st.markdown("[Go to Medical Data Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    st.markdown('<div class="back-button" style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Back", key="back_medical"):
        st.session_state.page = "main"
    st.markdown('</div>', unsafe_allow_html=True)

# Social Page
def social_page():
    st.write("### Social Data")
    st.markdown("[Go to Social Information Resource 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.markdown("[Go to Social Information Resource 2](https://torino.circololettori.it/gruppi-25-2/)")
    st.markdown("[Go to Social Information Resource 3](https://www.compagniadeimeglioinsieme.com/i-gruppi/gruppo-camminiamoinsieme-fitel-piemonte/)")
    st.markdown("[Go to Social Information Resource 4](https://www.promozionedellasalute.it/iniziative/comunita/gruppi-di-cammino)")
    st.markdown('<div class="back-button" style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Back", key="back_social"):
        st.session_state.page = "main"
    st.markdown('</div>', unsafe_allow_html=True)

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
