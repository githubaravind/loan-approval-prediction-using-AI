import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from contents.apply import display_app_form
from contents.info import display_info_form
from hooks import load_lottiefile
from predict import predict_loan
from contents.details import display_summary

#Lottie Files animation
lottie_decline = load_lottiefile("web/lottiefiles/decline.json") 
lottie_approved = load_lottiefile("web/lottiefiles/approved2.json") 


#Content Dialog
@st.dialog("Welcome to Loan Checker Ai by aravind reddy!")
def content_dialog(item):
    if item == "About the model.":
        return display_info_form()
    elif item == "Please fill up the application form.":
        st.session_state.open_new_application = False
        return display_app_form()
        
#Form Dialog    
@st.dialog("Welcome!")
def submitted_form_dialog():
    st.session_state.open_form_dialog = False
    st.write("Recent Submission Details:")
    st.markdown(f"""
    **Email:** {st.session_state.email['email']}                                           
    **Number of Dependent Family Members:** {st.session_state.df_submitted_details['dependents'].values[0]}  
    **Income:** {st.session_state.df_submitted_details['applicant_income'].values[0]}  
    **Additional Income:** {st.session_state.df_submitted_details['coapplicant_income'].values[0]}  
    **Loan Amount:** {st.session_state.df_submitted_details['loan_amount'].values[0]}  
    **Loan Amount Term:** {st.session_state.df_submitted_details['loan_amount_term'].values[0]}  
    **Credit History:** {st.session_state.df_submitted_details['credit_history'].values[0]}  
    **Property Area:** {st.session_state.df_submitted_details['property_area'].values[0]}
    """)
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit Another Application"):
            st.session_state.form_submitted = False
            st.session_state.submission_details = {}
            st.session_state.open_new_application = True
            st.rerun()
    with col2:
        if st.button("Get Loan"):
            st.session_state.open_result_dialog = True
            st.rerun()
            
#Results Dialog
@st.dialog("Result")
def result_dialog():
    st.session_state.open_new_application = False
    
    predict_loan()
    prediction = predict_loan()
    
    if prediction is None:
        st.error("Prediction could not be made.")
        return
    
    st.subheader('Prediction Result')
    if prediction == 1:
        st.write('Loan Approved')
        st_lottie(
            lottie_approved,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # medium ; high
            height=None,
            width=None,
            key=None,
        )
    else:
        st.write('Loan Rejected')
        st_lottie(
            lottie_decline,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # medium ; high
            height=None,
            width=None,
            key=None,
        )
    if st.button("Details"):
        st.session_state.open_details_dialog = True
        st.session_state.open_result_dialog = False
        st.rerun()
    display_summary()
    
    if st.button("Apply another loan"):
        st.session_state.form_submitted = False
        st.session_state.submission_details = {}
        st.session_state.open_new_application = True
        st.session_state.open_result_dialog = False
        st.rerun()    
    st.session_state.open_result_dialog = False
    

#Details Dialog
@st.dialog("Details")
def details_dialog():
    def display_data(key, description):
        """Helper function to display data with error handling."""
        st.write(description)
        if key in st.session_state:
            st.write(st.session_state[key])  # Display the dataset
        else:
            st.error(f"No {description.lower()} available.")

    display_data('df_submitted_details', "Submitted Details:")
    display_data('raw_dataset', "Raw Loan Dataset:")
    display_data('before_scaling_data', "Combined Dataset with selected features:")
    display_data('after_scaling_data', "Combined Dataset after scaling:")
    display_data('predicted_data', "Predicted Data:")

    st.session_state.open_details_dialog = False
    st.session_state.open_result_dialog = False
    
    if st.button("Apply another loan"):
        st.session_state.form_submitted = False
        st.session_state.submission_details = {}
        st.session_state.open_new_application = True
        st.session_state.open_result_dialog = False
        st.rerun()    
    
