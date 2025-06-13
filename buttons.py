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

/* General button styles */
button.custom-button {
    height: 100px; /* Button height */
    width: 200px; /* Button width */
    font-size: 18px; /* Font size */
    color: white; /* Text color */
    border-radius: 10px; /* Rounded corners */
    margin: 10px; /* Space between buttons */
    border: none; /* Remove border */
    cursor: pointer; /* Pointer cursor */
}

/* Unique button colors */
button.outdoor { background-color: #3498db; } /* Blue */
button.indoor { background-color: #2ecc71; } /* Green */
button.medical { background-color: #f39c12; } /* Orange */
button.social { background-color: #e74c3c; } /* Red */

/* Back button styles */
button.back-button {
    height: 40px; /* Smaller height */
    width: 80px; /* Smaller width */
    font-size: 14px; /* Smaller font size */
    background-color: #555; /* Dark gray */
    color: white; /* Text color */
    border-radius: 10px;
    border: none;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Main page
def main_page():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    # Custom HTML for buttons
    if st.markdown("<button class='custom-button outdoor' onclick='window.location.href=\"/outdoor\"'>Outdoor Environmental Data</button>", unsafe_allow_html=True):
        st.session_state.page = "outdoor"

    if st.markdown("<button class='custom-button indoor' onclick='window.location.href=\"/indoor\"'>Indoor Environmental Data</button>", unsafe_allow_html=True):
        st.session_state.page = "indoor"

    if st.markdown("<button class='custom-button medical' onclick='window.location.href=\"/medical\"'>Medical Data</button>", unsafe_allow_html=True):
        st.session_state.page = "medical"

    if st.markdown("<button class='custom-button social' onclick='window.location.href=\"/social\"'>Social Data</button>", unsafe_allow_html=True):
        st.session_state.page = "social"

    st.markdown("</div>", unsafe_allow_html=True)

# Outdoor Page
def outdoor_page():
    st.write("### Outdoor Environmental Data")
    st.markdown("[Go to Outdoor Information Resource](https://meteo.it)")
    if st.button("Back", key="back_outdoor", css_classes=["back-button"]):
        st.session_state.page = "main"

# Indoor Page
def indoor_page():
    st.write("### Indoor Environmental Data")
    st.markdown("[Go to Indoor Information Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.markdown("[Go to Indoor Information Dashboard 2](https://telefragmont-node2.streamlit.app/)")
    st.markdown("[Go to Indoor Information Dashboard 3](https://telefragmont-node3.streamlit.app/)")
    if st.button("Back", key="back_indoor", css_classes=["back-button"]):
        st.session_state.page = "main"

# Medical Page
def medical_page():
    st.write("### Medical Data")
    st.markdown("[Go to Medical Data Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    if st.button("Back", key="back_medical", css_classes=["back-button"]):
        st.session_state.page = "main"

# Social Page
def social_page():
    st.write("### Social Data")
    st.markdown("[Go to Social Information Resource 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.markdown("[Go to Social Information Resource 2](https://torino.circololettori.it/gruppi-25-2/)")
    st.markdown("[Go to Social Information Resource 3](https://www.compagniadeimeglioinsieme.com/i-gruppi/gruppo-camminiamoinsieme-fitel-piemonte/)")
    st.markdown("[Go to Social Information Resource 4](https://www.promozionedellasalute.it/iniziative/comunita/gruppi-di-cammino)")
    if st.button("Back", key="back_social", css_classes=["back-button"]):
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
