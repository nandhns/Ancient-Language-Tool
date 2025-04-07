import streamlit as st
import requests
import io
from PIL import Image
from navbar import navigation
st.title("Ancient Language Translation Tool")

uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(Image.open(uploaded_image), caption="Uploaded Image", use_container_width=True) #changed here.

    if st.button("Process Image"):
        # Send image to backend
        files = {'image': uploaded_image.getvalue()}

        try:
            response = requests.post("http://127.0.0.1:5000/translate", files=files)  # Replace with your API URL
            response.raise_for_status()
            data = response.json()

            # Display Results
            st.subheader("Detected Language:")
            st.write(data['script'])

            st.subheader("Translation:")
            st.write(data['translated_text'])

            st.subheader("Tags:")
            st.write(f"Demographic: {data.get('demographic', 'N/A')}")
            st.write(f"Era: {data.get('era', 'N/A')}")
            # Add more tags as needed

        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
        except KeyError:
            st.error("Invalid response from backend.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")