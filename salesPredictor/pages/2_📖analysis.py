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

num_feas_cat=list(num_vars)+num_cat  

st.header("SALES ANALYSIS:")




choice = st.sidebar.radio("Filters",["Histogram", "Box-plot", "Violen-plot","Pie Chart","Heatmap","Scatter"])
if choice == "Histogram":
    
    st.write("Histogram plotting")
    selection1 = st.selectbox("select column",options =list(set(num_feas_cat)))
    hist = px.histogram(df, x=selection1)
    st.plotly_chart(hist)
    

elif choice == "Box-plot":
    
    
    selection_x=st.selectbox("Select x coordinate (finite_categorical):",options=num_cat)
    selection_y=st.selectbox("Select y coordinate (continuous_numerical):",options=list(set(list(num_vars)).difference(num_cat)))

    box=px.box(df,x=selection_x,y=selection_y)
    st.plotly_chart(box)
    st.write("\n")

elif choice == "Violen-plot":
    
    st.write("Violin_Plot")
    selection_x1=st.selectbox("Select x1 coordinate (finite_categorical):",options=num_cat)
    selection_y1=st.selectbox("Select y1 coordinate (continuous_numerical):",options=list(set(list(num_vars)).difference(num_cat)))
    violin=px.violin(df,x=selection_x1,y=selection_y1,points="all")
    st.plotly_chart(violin)

    st.write("\n")

elif choice == "Pie Chart":
    st.write("Pie chart plotting")
    selection2 = st.selectbox("",options =num_cat)
    pie = px.pie(df, names=selection2)
    st.plotly_chart(pie)
    st.write("\n")

elif choice == "Heatmap":
    st.write("Heat Map")
    hmap = px.imshow(df.corr())
    st.plotly_chart(hmap)

    st.write("\n")

elif choice == "Scatter":
    st.write("Scatter plotting")
    selection_x2=st.selectbox("Select x2 coordinate (numerical):",options=list(set(list(num_vars)).difference(num_cat)))
    selection_y2=st.selectbox("Select y2 coordinate (numerical):",options=list(set(list(num_vars)).difference(num_cat)))
    none=[None]
    colors3=st.selectbox("Select the features for hue:",options=none+num_cat)

    try:
        scat=px.scatter(df,x=selection_x2,y=selection_y2,color=colors3)
        st.plotly_chart(scat)
    except KeyError:
        st.error("This column hue cannot be displayed because it contains NaN values")
    st.write("\n")
    st.markdown("**-------------------------------------------------------------------------------------------------**")
    st.write("\n")

