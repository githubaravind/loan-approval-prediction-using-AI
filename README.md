
# Loan Prediction with AI and Streamlit

[![Streamlit](https://img.shields.io/badge/Streamlit-Loan_Prediction_App-brightgreen.svg)](https://loan-approval-ai.streamlit.app/)

![image](https://github.com/user-attachments/assets/4b336e52-8283-498d-9e27-1c291c14ad9c)
![image](https://github.com/user-attachments/assets/cafd4dc5-e0af-4505-984b-f1f08a991d00)
![image](https://github.com/user-attachments/assets/35bfde4e-f17f-4a81-ac70-31333a4a6286)


This project demonstrates how **AI** and **Machine Learning** can be applied to **loan prediction** in the financial industry. By leveraging **Streamlit**, we've deployed a **Gaussian Naïve Bayes (GNB)** model that predicts loan approval based on user inputs. The aim is to create a seamless, automated process for loan applications, improving efficiency and accuracy.

## Demo

Try the loan prediction app here: [Loan Checker AI](https://loan-approval-ai.streamlit.app/)

---

## Features
- **Automated Loan Predictions**: Instantly predicts whether a loan will be approved or rejected based on user input.
- **Streamlit Deployment**: The app is deployed using Streamlit, offering an interactive and user-friendly experience.
- **Gaussian Naïve Bayes Model**: A machine learning model trained on a loan prediction dataset.
- **Real-Time Predictions**: The app processes user inputs in real-time to predict loan approval status.
  
## Dataset

The dataset used in this project contains 13 variables, including:
- **Loan_ID**: Unique loan reference number
- **ApplicantIncome**: The income of the applicant
- **LoanAmount**: The loan amount requested
- **Credit_History**: Key variable indicating the applicant's credit history
- **Property_Area**: The area of the applicant's residence (Urban, Semi-Urban, or Rural)
  
[Link to Dataset](https://www.kaggle.com/datasets/bhavikjikadara/loan-status-prediction)

## Model Overview

The loan prediction model is built using **Gaussian Naïve Bayes (GNB)**. Key performance metrics:
- **Training Accuracy**: 85.2%
- **Test Accuracy**: 81.82%

The model is trained to predict whether a loan will be approved based on various factors like credit history, income, and property area.

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/githubaravind/loan-approval-prediction-using-AI]```

### 2. Install the required packages
Ensure you have Python 3.6+ and the following packages installed:
```bash
pip install streamlit pandas scikit-learn joblib
```

### 3. Run the application
Navigate to the project directory and run the app:
```bash
streamlit run main.py
```
The app will be available at `http://localhost:8501`.

## Model Training

The model was trained on **Kaggle** using the loan prediction dataset. You can find the Kaggle notebook here:

- [Kaggle Notebook](https://www.kaggle.com/code/aravindreddy1468/loan-prediction)

For training, we used the following features:
- **Applicant Income**
- **Loan Amount**
- **Credit History**
- **Property Area**
- **Dependents**

## Exporting the Model

The trained model was exported using **Pickle** and **Joblib** for integration with the Streamlit app:
```python
from joblib import dump
dump(GNB, 'gnb_model.joblib')
```

## App Deployment

The app is deployed using **Streamlit Community Cloud**. To deploy the app yourself:
1. Push the repository to GitHub.
2. Log in to Streamlit.
3. Select your GitHub repository and deploy your app.

## File Structure

```plaintext
Loan-Prediction/
│
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── dataset/
│   └── processed_dataset.csv  # Cleaned dataset used for prediction
├── models/
│   └── gnb_model.pkl    # Trained model
├── web/
│   ├── main.py          # Main application script
│   ├── predict.py       # Prediction logic
│   ├── dialogs.py       # Dialogs and UI elements
│   └── hooks.py         # Utility functions
└── README.md            # Project documentation
```

## Contributing

Feel free to fork this repository, submit issues, or open pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Kaggle Community** for the loan prediction dataset and analysis tools.
- **Streamlit** for providing an easy-to-use deployment framework.
- Special thanks to **Hassan** for the insightful Exploratory Data Analysis (EDA) on the dataset.

---

If you found this project helpful or have any questions, feel free to reach out!

---



