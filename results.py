import streamlit as st
from navbar import navigation

st.title("Ancient Language Translation Tool")

# Mock Results (Replace with your actual data structure)
mock_results = {
    "script": "Ancient Egyptian Hieroglyphs",
    "translated_text": "This is a mock translation.",
    "demographic": "Pharaohs and Scribes",
    "era": "New Kingdom",
    "predicted_text": "Possible continuation: ... and their scribes recorded these words."
}

# Display Mock Results
st.subheader("Detected Language:")
st.write(mock_results["script"])

st.subheader("Translation:")
st.write(mock_results["translated_text"])

st.subheader("Tags:")

# Display tags as badges
st.markdown(
    f"""
    <style>
    .tag-badge {{
        background-color: #e1f5fe;
        color: #01579b;
        padding: 5px 10px;
        border-radius: 15px;
        margin-right: 5px;
        display: inline-block;
        font-size: 14px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(f'<span class="tag-badge">Demographic: {mock_results["demographic"]}</span>', unsafe_allow_html=True)
st.markdown(f'<span class="tag-badge">Era: {mock_results["era"]}</span>', unsafe_allow_html=True)
st.markdown(f'<span class="tag-badge">Predicted: {mock_results["predicted_text"]}</span>', unsafe_allow_html=True)

st.subheader("Additional Notes:")
st.write("This is a mock-up. Replace with actual data once the backend is connected.")