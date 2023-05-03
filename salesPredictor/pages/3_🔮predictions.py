import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px


df=pd.read_csv("Train.csv")



columns=df.columns
num_vars=df.select_dtypes(include=["int64","float64"]).columns # selecting the int and float datatype columns
cat_vars=df.select_dtypes(include=["object"]).columns # selecting the object datatype column


num_cat=[]
for i in list(num_vars):
    if (len(df[i].unique())<=20): 
        num_cat.append(i)  # now num_cat contains discrete numerical features.

num_obj=[]
for i in list(cat_vars):
    if (len(df[i].unique())<=20): 
        num_obj.append(i)  # now num_obj contains columns with finite categories.


num_cat=num_cat+num_obj # now it contains all the columns which have not more than 20 unique categories


st.write("\n")






num_feas_cat=list(num_vars)+num_cat

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 30px;">User Inputs for outlet sales prediction</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.write("\n")



new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Item Weight:</p>'
st.markdown(new_title, unsafe_allow_html=True)
wei=st.number_input("",value=2.0)
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Fat Type:</p>'
st.markdown(new_title, unsafe_allow_html=True)
fat=st.selectbox("",["Low Fat","Regular"])
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed   ; font-size: 20px;">Visibility of the brand:</p>'
st.markdown(new_title, unsafe_allow_html=True)
visible= st.slider("",min_value=0.0,max_value=1.0,value=0.05)
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Item Categories</p>'
st.markdown(new_title, unsafe_allow_html=True)
types=st.radio("",['Fruits and Vegetables', 'Snack Foods', 'Household', 'Frozen Foods', 'Dairy', 'Canned', 'Baking Goods', 'Health and Hygiene', 'Soft Drinks', 'Meat', 'Breads', 'Hard Drinks', 'Others', 'Starchy Foods', 'Breakfast', 'Seafood'])
st.write("\n")


new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">MRP of the item:</p>'
st.markdown(new_title, unsafe_allow_html=True)
mrp=st.number_input("",value=1.0)
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed ; font-size: 20px;">Outlet Identifier code:</p>'
st.markdown(new_title, unsafe_allow_html=True)
out_id=st.selectbox("",['OUT027', 'OUT013', 'OUT046', 'OUT049', 'OUT035', 'OUT045', 'OUT018', 'OUT017', 'OUT010', 'OUT019'])
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed   ; font-size: 20px;">Outlet Est. Year:</p>'
st.markdown(new_title, unsafe_allow_html=True)
year_1=st.slider("",min_value=1970,max_value=2020)
year=2021-year_1
st.write("\n")


new_title = '<p style="font-family:sans-serif; color:DarkRed   ; font-size: 20px;">Outlet type (size of export):</p>'
st.markdown(new_title, unsafe_allow_html=True)
ot=st.selectbox("",['Small','Medium','High'])
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Output Location Type</p>'
st.markdown(new_title, unsafe_allow_html=True)
oloc=st.radio("",['Tier 1', 'Tier 2', 'Tier 3'])
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Store Type</p>'
st.markdown(new_title, unsafe_allow_html=True)
os=st.selectbox("",['Supermarket Type1', 'Grocery Store', 'Supermarket Type3', 'Supermarket Type2'])
st.write("\n")

means=[12.813419570574444,0, 0.06613202877895127,0, 140.9927819781768,0, 23.168133286401503,0,0,0]
stds=[4.226992409024986,0, 0.05159479525696192,0, 62.271413051361094,0, 8.37126926612472,0,0,0]



dic={'Baking Goods': 6,
 'Breads': 10,
 'Breakfast': 14,
 'Canned': 5,
 'Dairy': 4,
 'Frozen Foods': 3,
 'Fruits and Vegetables': 0,
 'Grocery Store': 1,
 'Hard Drinks': 11,
 'Health and Hygiene': 7,
 'High': 2,
 'Household': 2,
 'Low Fat': 0,
 'Meat': 9,
 'Medium': 0,
 'OUT010': 8,
 'OUT013': 1,
 'OUT017': 7,
 'OUT018': 6,
 'OUT019': 9,
 'OUT027': 0,
 'OUT035': 3,
 'OUT045': 5,
 'OUT046': 4,
 'OUT049': 2,
 'Others': 12,
 'Regular': 1,
 'Seafood': 15,
 'Small': 1,
 'Snack Foods': 1,
 'Soft Drinks': 8,
 'Starchy Foods': 13,
 'Supermarket Type1': 0,
 'Supermarket Type2': 3,
 'Supermarket Type3': 2,
 'Tier 1': 2,
 'Tier 2': 1,
 'Tier 3': 0}

trees=pickle.load(open("treex.pkl","rb"))
par=[wei,fat,visible,types,mrp,out_id,year,ot,oloc,os] # parameters for the model

for i in range(len(par)): #label encoding and scaling the parameters
  if i in [0,2,4,6]:
    par[i]=(par[i]-means[i])/stds[i]

  else:
    par[i]=dic[par[i]]
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:GREEN; font-size: 30px;">PREDICT THE SALES</p>'
st.markdown(new_title, unsafe_allow_html=True)
if st.button("Predict"):
    pred=trees.predict([par])
    
    st.write("The Outlet Sales Value is:",pred[0])