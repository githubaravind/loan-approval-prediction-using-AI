import streamlit as st
import os
from dialogs import content_dialog, submitted_form_dialog, result_dialog, details_dialog
from hooks import set_png_as_page_bg

# Constants
BACKGROUND_IMAGE = 'web/images/blank-bg.png'
CSS_FILE_PATH = "web/styles/styles.css"
INFO_DIALOG = "About the model."
APPLICATION_DIALOG = "Please fill up the application form."
LOGO_URL = 'web/images/logo.png'


# Set the background image
set_png_as_page_bg(BACKGROUND_IMAGE)

# Initialize session state
if "content" not in st.session_state:
    st.session_state.content = None

# Display logo and title
st.logo(LOGO_URL)
st.divider()
st.markdown('<h1 style="font-size:50px;color:#187078;">Bank Loan Checker</h1>', unsafe_allow_html=True)
st.divider()


col1, col2 = st.columns(2)

def handle_button_click(item, dialog_message):
    # Reset dialog states
    st.session_state.open_results_dialog = False
    st.session_state.open_details_dialog = False
    st.session_state.open_new_application = False
    st.session_state.content = {"item": item, "reason": content_dialog(dialog_message)}

# Create a container for the buttons
with st.container():
    st.caption("Innovative and real-time project on Loan Approval Prediction Using Machine Learning")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Info"):
            handle_button_click("Info", INFO_DIALOG)

    with col2:
        if st.button("Apply"):
            handle_button_click("Apply", APPLICATION_DIALOG)

# Display reason if available
if st.session_state.content and st.session_state.content.get('reason'):
    st.write(st.session_state.content['reason'])

# Display dialogs based on session state
if st.session_state.get("open_new_application", False):
    content_dialog(APPLICATION_DIALOG)

# Display recent submission details if available
if st.session_state.get("form_submitted") and st.session_state.get("open_form_dialog", False):
    submitted_form_dialog()

# Display result if success_modal is True
if st.session_state.get("open_result_dialog", False):
    result_dialog()

# Display the details of the predicted value
if st.session_state.get("open_details_dialog", False):
    details_dialog()


# Check if the CSS file exists before attempting to open it
def load_css(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found: {file_path}")

load_css(CSS_FILE_PATH)