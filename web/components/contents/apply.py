import streamlit as st
import pandas as pd

def display_app_form():

    st.caption("Please fill up the application form")
    
    # Input fields
    email = st.text_input("Email", placeholder="Enter your email")
    family_members = st.selectbox("Number of people you are providing", ["0", "1", "2", "3+"])
    income = st.text_input("Annual Income ($)", placeholder="Enter your annual income in USD")
    additional_income = st.text_input("Annual Additional Income ($)", placeholder="Enter your additional annual income from other sources")
    loan_amount = st.text_input("Loan Amount ($)", placeholder="Enter the amount you want to loan")

    loan_term = st.text_input("Loan Amount Term (days)", placeholder="Enter the loan's repayment period (in days)")
    credit_history = 1 if st.radio("Do you have a credit history?", ["Yes", "No"]) == "Yes" else 0
    property_location = st.selectbox("Property Location", ["Rural", "Urban", "Semiurban"])
    terms_accepted = st.checkbox("I accept the terms and conditions.")

    # Validate inputs
    if st.button("Submit Application"):
        if not all([email, loan_amount, loan_term, property_location]) or not terms_accepted:
            st.error("All fields are required and terms must be accepted.")
            return None

        try:
            # Convert and validate numeric inputs
            loan_amount, income, additional_income, loan_term = map(lambda x: round(float(x), 2), [loan_amount, income, additional_income, loan_term])
            if any(x < 0 for x in [loan_amount, loan_term, income, additional_income]):
                raise ValueError("Values must be positive numbers or zero.")
        except ValueError:
            st.error("Please enter valid positive numbers for Loan Amount, Loan Term, Income, and Additional Income.")
            return None

        # Store submitted details
        st.session_state.email = {"email": email}
        st.session_state.df_submitted_details = pd.DataFrame({
            "dependents": [family_members],
            "applicant_income": [f"{income:.2f}"],
            "coapplicant_income": [f"{additional_income:.2f}"],
            "loan_amount": [f"{loan_amount:.2f}"],
            "loan_amount_term": [loan_term],
            "credit_history": [credit_history],
            "property_area": [property_location]
        })
        st.session_state.form_submitted = True
        st.session_state.open_form_dialog = True
        st.rerun()

    # Show success dialog if form is submitted
    if st.session_state.get("form_submitted"):
        st.session_state.form_submitted = False
    return None