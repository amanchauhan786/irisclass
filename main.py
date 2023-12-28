import streamlit as st
import joblib

# Load the trained model
model = joblib.load('trained_model.joblib')

# Streamlit app title
st.title("Iris Flower Classification App :hibiscus:")

# Take input values from the user
sepal_length = st.slider("Enter sepal length:", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
sepal_width = st.slider("Enter sepal width:", min_value=0.0, max_value=10.0, value=3.0, step=0.1)
petal_length = st.slider("Enter petal length:", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
petal_width = st.slider("Enter petal width:", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

# Make predictions using the input values
result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]

# Display the prediction result
st.markdown(
            f"""
            <p style='font-family:"Bold", Gadget, sans-serif; font-size: 25px; color: White;font-weight:Bold'>The predicted class is:</p>
            """,
            unsafe_allow_html=True)
st.markdown(
            f"""
            <p style='font-family:"Bold", Gadget, sans-serif; font-size: 30px; color: White;font-weight:Bold'>{result}</p>
            """,
            unsafe_allow_html=True)
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://images.fineartamerica.com/images-medium-large-5/purple-magic-camille-lopez.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()