import streamlit as st  

def display_summary():
    st.write("**How Key Features Affect Loan Approval 🧐**")
    st.write("The following factors play a significant role in determining whether a loan is approved or rejected:")
    
    st.write("1. **Applicant Income 💼**")
    st.write("- **High Income**: Increases the likelihood of approval because higher income means better repayment ability.")

    st.write("- **Low Income**: Could lead to rejection as the bank may see the applicant as less capable of repaying the loan on time.")
    
    st.write("2. **Coapplicant Income 🤝**")
    st.write("- **High Coapplicant Income**: Helps increase the chances of approval, especially if the primary applicant’s income is low. The combined income provides more security for the lender.")

    st.write("- **Low Coapplicant Income**: May not help much if the primary applicant’s income is insufficient.")
    
    st.write("3. **Loan Amount 💵**")
    st.write("- **High Loan Amount**: A larger loan increases risk for the bank, so approval is less likely unless the income and credit history are strong.")
    st.write("- **Low Loan Amount**: Easier to approve as it represents a lower financial risk.")
    
    st.write("4. **Loan Amount Term 📆**")
    st.write("- **Longer Terms (e.g., 360 days)**: A longer repayment period may reduce monthly payments, making it easier for lower-income applicants to get approval.")
    st.write("- **Shorter Terms (e.g., 120 days)**: Could lead to rejection if the monthly payments are too high for the applicant's income.")
    
    st.write("5. **Credit History 🏦**")
    st.write("- **Good Credit History (1)**: Significantly boosts approval chances. A solid repayment track record shows the applicant is reliable.")

    st.write("- **Bad Credit History (0)**: A bad credit history often results in immediate rejection, as the bank sees the applicant as high-risk.")
    
    st.write("6. **Dependents 👨‍👩‍👧‍👦**")
    st.write("- **Few or No Dependents**: Fewer financial obligations mean more disposable income, which increases the chances of approval.")
    st.write("- **Many Dependents**: A higher number of dependents could reduce approval chances as the applicant may have less available income to repay the loan.")
    
    st.write("7. **Property Area 🌍**")
    st.write("- **Urban or Semi-urban Areas**: These areas typically have higher property values and better economic conditions, making approval more likely.")

    st.write("- **Rural Areas**: Loans for properties in rural areas might be seen as riskier, leading to potential rejection depending on the applicant's financials.")
    
    st.write("**Example Scenarios**")
    st.write("- **Low Income + High Loan Amount**: Likely to be rejected because the applicant may struggle to make payments.")

    st.write("- **Bad Credit History + Many Dependents**: Could result in rejection due to the high perceived risk of default.")

    st.write("- **High Income + Long Loan Term**: Likely to be approved because the monthly payments are manageable, and the applicant has sufficient income.")
    
    st.write("In real life, a balance of these features is critical. Strong income and good credit history can overcome a higher loan amount, but low income or poor credit will likely lead to rejection, even for smaller loans.")