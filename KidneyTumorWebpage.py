import streamlit as st

st.set_page_config(page_title="New webpage")

st.title("Kidney Tumor Detection Webpage:open_book:")
st.write(
    "Kidney cancer also known as renal cell carcinoma (RCC), continues to be a significant health concern in current days.It's a top-10 cancer globally,sees improved diagnostics, minimally invasive surgeries, and advanced treatments like targeted therapies and immunotherapies, enhancing outcomes and patient quality of life in recent years. Continued research and awareness remain vital for further progress.")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.image("https://www.netmeds.com/images/cms/wysiwyg/blog/2019/11/KidneyCancer_big_898.jpg",
                 use_column_width=True)
    with right_column:
        st.write("##")
        st.image(
            "https://images.ctfassets.net/yixw23k2v6vo/6dMTw6KW0Q3p84Ujvaxq5o/67253b2f1741eddcf471578ce512be4d/INFO_KIDNEY_stats.png?fit=thumb&w=640&h=360",
            use_column_width=True)
with st.container():
    st.write("---")
    st.write("""
                Kidney cancer treatment varies depending on factors like cancer type, stage, and overall health. Options include:

                1) Active Surveillance: Monitoring small tumors for growth.

                2) Thermal Ablation: Destroying tumors with heat or cold for select early-stage cases.

                3) Surgery (Nephrectomy): Removing part or all of the kidney, often curative.

                4) Drug Therapy: For advanced cases:

                    i) Immunotherapy: Boosting the immune system to combat cancer.

                    ii) Targeted Therapy: Inhibiting cancer cell growth and blood vessel formation.

                Treatment choices depend on individual circumstances, with a focus on preserving kidney function and managing side effects.
                Advanced therapies like immunotherapy and targeted therapy offer promising options for patients with advanced kidney cancer.
            """)

with st.container():
    st.write("---")
    st.header("Upload Images to Check for Kidney Tumor")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
st.write("This is my Streamlit app with a light blue background.")
