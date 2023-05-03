import streamlit as st

new_title1 = '<p style="font-family:sans-serif; text-align:center; color:yellow  ; font-size: 20px;">About the Project: </p>'
st.markdown(new_title1, unsafe_allow_html=True)

st.write('Keeping track of individual item sales data in order to forecast future client demand, adjust inventory management and the popularity of that given product in a region to adjust shipping quotas has become a very important aspect of automating demand for big supermarkets, where the amount of iteams and goods processed are very high. The sales and other associated data for this purpose are collected from various sources and stored in data warehouses across the country to optimize for analytics purposes. By carefully mining and processing this data, interesting visualization, various anomalies and many interesting patterns can be found. This data is finally used to optimize profit and loss for the respective retailer.')

new_title2 = '<p style="font-family:sans-serif; text-align:center; color:yellow  ; font-size: 20px;">Approach: </p>'
st.markdown(new_title2, unsafe_allow_html=True)

st.write('🔯Data Exploration : Read the dataset using pandas and numpy to find null values, categorical and numerical columns from the given dataset  \n 🔯Data Visualization : Performed Exploratory Data Analysis, to gain insights and learn the correlation of the columns with the output variable.    \n 🔯Feature Engineering : Removed missing values and normalize the dataset to feed the values to the ML model.   \n 🔯Model Building : Build simple and ensemble regression models to check base accuracy and mean squared error. Then compare the models to find the best possible model.     \n 🔯Deployment : Using Streamlit built a webapp, to predict the Item_Outlet_Sales provided all necessary inputs are provided')





