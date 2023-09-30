import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array

st.set_page_config(page_title="New webpage")

st.markdown(
    """
    <style>
        /* Style for st.title */
        h1 {
            color: #add8e6; /* Text color */
            background-color: #000000;
            font-size: 24px; /* Font size */
            text-align: center; /* Text alignment */
            margin-bottom: 20px; /* Margin bottom */
        }
        .st-emotion-cache-fg4pbf{
        background-color: #C8E6C9;
        background-image: url("https://th.bing.com/th/id/OIP.lyr_v0djY0gv9_vkRICBDwAAAA?pid=ImgDet&rs=1");
        background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


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
    # st.header("Upload Images to Check for Kidney Tumor")
    #st.title("Kidney Tumor Classification")

    st.header("Please upload an Image")

    file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

    model = load_model("C:/Users/cirim/PycharmProjects/Python1/model1.h5")


    def classification(file, model):
        img_path = file
        img = load_img(img_path, target_size=(224, 224))  # Adjust the target size if needed
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Rescale to match the training data preprocessing

        # Make predictions using the provided model
        prediction = model.predict(img_array)
        p = 0
        # Determine the class label based on the prediction
        if prediction[0, 0] > 0.5:
            # print("prediction",prediction[0,0])
            class_label = 'Tumor'
            prediction = prediction[0, 0]
            p = prediction * 100
        else:
            class_label = 'Normal'
            prediction = prediction[0, 0]
            p = (100 - (prediction * 100))
        return class_label, prediction, p


    if file is not None:
        image = Image.open(file).convert('RGB')
        st.image(image, use_column_width=True)
        detect_button = st.button("Detect")
        if detect_button:
            class_name, prediction, p = classification(file, model)
            # print(class_name)
            st.write("## {}".format(class_name))
            # st.write("### score: {}".format(prediction))
            st.write("### Predicted value: {}".format(p))
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
