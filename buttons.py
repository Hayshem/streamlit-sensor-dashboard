import streamlit as st

# Main page
def main_page():
    # Custom HTML for buttons
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; gap: 20px; padding: 20px;">
        <form action="#" method="post" style="display: inline;">
            <button type="submit" name="page" value="outdoor" style="height: 100px; width: 200px; font-size: 18px; border-radius: 10px; border: none; cursor: pointer; background-color: #3498db; color: white;">Outdoor Environmental Data</button>
        </form>
        <form action="#" method="post" style="display: inline;">
            <button type="submit" name="page" value="indoor" style="height: 100px; width: 200px; font-size: 18px; border-radius: 10px; border: none; cursor: pointer; background-color: #2ecc71; color: white;">Indoor Environmental Data</button>
        </form>
        <form action="#" method="post" style="display: inline;">
            <button type="submit" name="page" value="medical" style="height: 100px; width: 200px; font-size: 18px; border-radius: 10px; border: none; cursor: pointer; background-color: #f39c12; color: white;">Medical Data</button>
        </form>
        <form action="#" method="post" style="display: inline;">
            <button type="submit" name="page" value="social" style="height: 100px; width: 200px; font-size: 18px; border-radius: 10px; border: none; cursor: pointer; background-color: #e74c3c; color: white;">Social Data</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

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
