import streamlit as st

from predict import  predict_sales
st.title("Sales Predictor App")

st.image("sales.jpeg")


tv_sales = st.number_input("Enter the sales rate of TV", 0,100,0)

radio_sales =st.number_input("Enter the sales rate of Radio", 0, 100, 0)


if st.button("Predict"):
    input = [[tv_sales, radio_sales]]

    prediction = predict_sales(input)
    st.write(prediction[0])

    if (prediction[0]>=50):
        st.success("You have good sales brother!")
    else:
        st.warning("You have to up the gear brother!")