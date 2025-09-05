import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler, LabelEncoder

def predict_loan():
    # Load the dataset
    dataset = pd.read_csv('dataset/processed_dataset.csv')
    st.session_state.raw_dataset = dataset
    
    # Combine submitted data with the dataset
    combined_data = pd.concat([st.session_state.df_submitted_details, dataset], ignore_index=True)
    st.session_state.before_scaling_data = combined_data.copy()
    
    # Scale numerical features
    scaled_features = ["applicant_income", "coapplicant_income", "loan_amount", "loan_amount_term"]
    scaler = StandardScaler()
    combined_data[scaled_features] = scaler.fit_transform(combined_data[scaled_features])
    st.session_state.after_scaling_data = combined_data.copy()
    
    # Encode categorical features
    categorical_features = combined_data.select_dtypes(include=['object']).columns
    label_encoder = LabelEncoder()
    for column in categorical_features:
        combined_data[column] = label_encoder.fit_transform(combined_data[column].astype(str))
    
    # Drop unnecessary columns
    columns_to_drop = ['education', 'gender', 'married', 'self_employed']
    scaled_data = combined_data.drop(columns=columns_to_drop, errors='ignore')
    st.session_state.selected_features_data = scaled_data.copy()
    st.session_state.predicted_data = scaled_data.iloc[0:1]
    
    # Load the model
    try:
        with open('models/gnb_model.pkl', 'rb') as gnb:
            model = pickle.load(gnb)
    except FileNotFoundError:
        st.error("Model file not found.")
        return
    
    # Make a prediction
    try:
        prediction = model.predict(scaled_data.iloc[0:1])
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None
    
    return prediction[0]  # Return the prediction directly