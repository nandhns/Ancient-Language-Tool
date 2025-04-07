import streamlit as st

st.set_page_config(layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Translate"

def navigation():
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 3])

    with col1:
        st.markdown("## Home")

    with col2:
        st.markdown("## Translate")
    
    with col3:
        st.markdown("## About")

    with col4:
        st.markdown("## Browse")

    with col5:
        search_query = st.text_input("Search", placeholder="Enter search term...")
        if search_query:
            st.write(f"Searching for: {search_query}")

navigation()