import streamlit as st

# Main page
def main_page():
    # Create a grid layout for buttons
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Outdoor Environmental Data Button
        if st.button("Outdoor Environmental Data", use_container_width=True, key="outdoor"):
            st.session_state.page = "outdoor"

        # Indoor Environmental Data Button
        if st.button("Indoor Environmental Data", use_container_width=True, key="indoor"):
            st.session_state.page = "indoor"

    with col2:
        # Medical Data Button
        if st.button("Medical Data", use_container_width=True, key="medical"):
            st.session_state.page = "medical"

        # Social Data Button
        if st.button("Social Data", use_container_width=True, key="social"):
            st.session_state.page = "social"

# Outdoor Page
def outdoor_page():
    st.write("### Outdoor Environmental Data")
    st.markdown("[Go to Outdoor Data Dashboard](https://meteo.it)")
    st.button("Back", on_click=lambda: setattr(st.session_state, "page", "main"))

# Indoor Page
def indoor_page():
    st.write("### Indoor Environmental Data")
    st.markdown("[Go to Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.markdown("[Go to Dashboard 2](https://example.com/indoor-2)")
    st.button("Back", on_click=lambda: setattr(st.session_state, "page", "main"))

# Medical Page
def medical_page():
    st.write("### Medical Data")
    st.markdown("[Go to Medical Data Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    st.button("Back", on_click=lambda: setattr(st.session_state, "page", "main"))

# Social Page
def social_page():
    st.write("### Social Data")
    st.markdown("[Go to Social Data Dashboard 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.markdown("[Go to Social Data Dashboard 2](https://example.com/social-2)")
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
