import streamlit as st

# Define custom HTML and JavaScript for navigation
def main_page():
    st.markdown("""
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px;">
            <a href="#" onclick="Streamlit.setComponentValue('outdoor')"
               style="display: inline-block; text-decoration: none; background-color: #3498db;
                      color: white; padding: 20px 40px; border-radius: 10px; font-size: 18px;
                      text-align: center; cursor: pointer; width: 200px;">
               Outdoor Environmental Data
            </a>
            <a href="#" onclick="Streamlit.setComponentValue('indoor')"
               style="display: inline-block; text-decoration: none; background-color: #2ecc71;
                      color: white; padding: 20px 40px; border-radius: 10px; font-size: 18px;
                      text-align: center; cursor: pointer; width: 200px;">
               Indoor Environmental Data
            </a>
            <a href="#" onclick="Streamlit.setComponentValue('medical')"
               style="display: inline-block; text-decoration: none; background-color: #f39c12;
                      color: white; padding: 20px 40px; border-radius: 10px; font-size: 18px;
                      text-align: center; cursor: pointer; width: 200px;">
               Medical Data
            </a>
            <a href="#" onclick="Streamlit.setComponentValue('social')"
               style="display: inline-block; text-decoration: none; background-color: #e74c3c;
                      color: white; padding: 20px 40px; border-radius: 10px; font-size: 18px;
                      text-align: center; cursor: pointer; width: 200px;">
               Social Data
            </a>
        </div>
        <script>
            function Streamlit() {
                return {
                    setComponentValue: function(value) {
                        const event = new CustomEvent('streamlit:input', {
                            detail: { data: value }
                        });
                        window.dispatchEvent(event);
                    }
                }
            }
        </script>
    """, unsafe_allow_html=True)

def outdoor_page():
    st.write("### Outdoor Environmental Data")
    st.markdown("[Go to Outdoor Information Resource](https://meteo.it)")
    if st.button("Back"):
        st.session_state.page = "main"

def indoor_page():
    st.write("### Indoor Environmental Data")
    st.markdown("[Go to Indoor Dashboard 1](https://telefragmont-node1.streamlit.app/)")
    st.markdown("[Go to Indoor Dashboard 2](https://telefragmont-node2.streamlit.app/)")
    st.markdown("[Go to Indoor Dashboard 3](https://telefragmont-node3.streamlit.app/)")
    if st.button("Back"):
        st.session_state.page = "main"

def medical_page():
    st.write("### Medical Data")
    st.markdown("[Go to Medical Dashboard](https://www.statista.com/topics/6349/healthcare-system-in-italy/)")
    if st.button("Back"):
        st.session_state.page = "main"

def social_page():
    st.write("### Social Data")
    st.markdown("[Go to Social Resource 1](http://www.digi.to.it/2021/10/07/gruppi-di-lettura-a-torino-quali-seguire/)")
    st.markdown("[Go to Social Resource 2](https://torino.circololettori.it/gruppi-25-2/)")
    st.markdown("[Go to Social Resource 3](https://www.compagniadeimeglioinsieme.com/i-gruppi/gruppo-camminiamoinsieme-fitel-piemonte/)")
    st.markdown("[Go to Social Resource 4](https://www.promozionedellasalute.it/iniziative/comunita/gruppi-di-cammino)")
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
