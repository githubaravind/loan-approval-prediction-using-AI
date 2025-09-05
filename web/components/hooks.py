import json
import base64
import requests  # pip install requests
import streamlit as st  # pip install streamlit

#Lottie Files
def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Lottie file not found: {filepath}")
        return None

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#For setting up the background image
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"File not found: {bin_file}")
        return None

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;

        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
