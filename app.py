import streamlit as st
from models.predict import PDFPredictor


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="PDF Page Classification AI",
    page_icon="📄",
    layout="wide"
)


# -------------------------------
# Title
# -------------------------------

st.title("📄 PDF Page Classification using AI")
st.write(
    "Upload your PDF document and classify each page using AI."
)


# -------------------------------
# Upload PDF
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)


if uploaded_file:

    st.success("PDF Uploaded Successfully ✅")


    st.subheader("📌 File Information")

    st.write(
        f"File Name : {uploaded_file.name}"
    )

    st.write(
        f"File Size : {round(uploaded_file.size/1024,2)} KB"
    )


    # -------------------------------
    # Classification Button
    # -------------------------------

    if st.button("🚀 Start Classification"):


        with st.spinner("Analyzing PDF..."):


            predictor = PDFPredictor()


            results = predictor.predict(uploaded_file)



        st.success("Classification Completed ✅")


        # -------------------------------
        # Display Results
        # -------------------------------

        st.subheader("📊 Classification Results")


        if results:


            for index, result in enumerate(results):

                st.markdown(
                    f"### Page {index+1}"
                )


                st.write(result)


                st.divider()


        else:

            st.warning(
                "No results found"
            )