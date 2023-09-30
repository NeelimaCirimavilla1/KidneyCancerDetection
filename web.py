import streamlit as st

def main():
    st.title("Kidney Tumor Detection")
    
    uploaded_image = st.file_uploader("Upload CT Scan", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        detect_button = st.button("Detect")
        
        if detect_button:
            # Perform image detection logic by attaching ai model pthon file here)
            st.write("Image detected as of now!")

if __name__ == "__main__":
    main()
