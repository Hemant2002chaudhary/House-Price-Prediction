import streamlit as st
import joblib
import pandas as pd

model = joblib.load('house_price_model.pkl')

st.title('House Price Predictor')

area = st.number_input('Area (sqft)', min_value=0)
bedrooms = st.number_input('Bedrooms', min_value=0)

if st.button('Predict Price'):
    input_data = pd.DataFrame({'area': [area], 'bedrooms': [bedrooms]})
    price = model.predict(input_data)[0]
    st.write(f'Predicted Price: ${price:,.2f}')