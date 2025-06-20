import streamlit as st

# Inject custom CSS for styling buttons
st.markdown("""
    <style>
        /* Base button style with consistent sizes */
        .custom-button {
            height: 100px; /* Set button height */
            width: 200px; /* Set button width */
            font-size: 16px; /* Font size for button text */
            margin: 10px; /* Space between buttons */
            border-radius: 8px; /* Rounded corners */
            color: white; /* Text color */
            border: none; /* Remove border */
            cursor: pointer; /* Pointer cursor */
            display: inline-block; /* Align buttons */
            text-align: center; /* Center text */
        }

        /* Unique colors for each button */
        .outdoor {
            background-color: #3498db; /* Blue */
        }
        .indoor {
            background-color: #2ecc71; /* Green */
        }
        .medical {
            background-color: #f39c12; /* Orange */
        }
        .social {
            background-color: #e74c3c; /* Red */
        }

        /* Hover effects */
        .outdoor:hover {
            background-color: #2980b9; /* Darker blue */
        }
        .indoor:hover {
            background-color: #27ae60; /* Darker green */
        }
        .medical:hover {
            background-color: #d35400; /* Darker orange */
        }
        .social:hover {
            background-color: #c0392b; /* Darker red */
        }
    </style>
""", unsafe_allow_html=True)

# Main page
def main_page():
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    # Arrange buttons in two rows
    st.markdown("""
        <div style="display: flex; flex-wrap: wrap; justify-content: center;">
            <button class="custom-button outdoor" onclick="window.location.href='?page=outdoor'">Outdoor Environmental Data</button>
            <button class="custom-button indoor" onclick="window.location.href='?page=indoor'">Indoor Environmental Data</button>
            <button class="custom-button medical" onclick="window.location.href='?page=medical'">Medical Data</button>
            <button class="custom-button social" onclick="window.location.href='?page=social'">Social Data</button>
        </div>
    """, unsafe_allow_html=True)

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
