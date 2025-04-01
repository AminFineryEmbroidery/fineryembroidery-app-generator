import streamlit as st

st.set_page_config(page_title="FineryEmbroidery Generator", layout="centered")
st.title("FineryEmbroidery Product Generator")

uploaded_files = st.file_uploader("Upload product images", accept_multiple_files=True)

if uploaded_files:
    st.image(uploaded_files[0], caption="Main Image for Description", use_column_width=True)
    st.success("Images received. OCR & generation logic to be added here.")