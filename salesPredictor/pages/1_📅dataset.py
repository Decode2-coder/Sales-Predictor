import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px

df=pd.read_csv("Train.csv")

columns=df.columns
num_vars=df.select_dtypes(include=["int64","float64"]).columns # selecting the int and float datatype columns
cat_vars=df.select_dtypes(include=["object"]).columns # 

num_cat=[]
for i in list(num_vars):
    if (len(df[i].unique())<=20): 
        num_cat.append(i)  # now num_cat contains discrete numerical features.

num_obj=[]
for i in list(cat_vars):
    if (len(df[i].unique())<=20): 
        num_obj.append(i)  # now num_obj contains columns with finite categories.


num_cat=num_cat+num_obj

choice = st.sidebar.radio("Filters",["dashboard", "description","overview"])
if choice == "dashboard":
    st.subheader("SALES DASHBOARD")
    st.dataframe(data=df)
    st.write("\n")

elif choice == "description":
    st.subheader("Description:")
    st.write("\n")
    st.write(df.describe())
    st.write("\n")




elif choice == "overview":
    st.subheader("Unique Values: ")
    st.write("\n")
    st.subheader("Select multiple columns to view simultaneously:")
    st.write("\n")
    cb_selcol=st.multiselect("",list(df.columns))
    if cb_selcol is not None:
        st.write(df[cb_selcol])
        st.write("\n")
        st.subheader("Unique categories and Value counts:")
        if st.checkbox("Click the checkbox for finding unique categories and valuecounts"):
            st.write("\n")
            if num_cat is not None:
                for i in num_cat:
                    if (len(df[i].unique())>20):

                        st.write(i,"Column is not shown because it has more than 20 unique categories")
                        st.markdown("**-------------------------------------------------------------------------------------------------**")
                        pass
                    else:
                        st.write("Unique categories in ",i,"column:",df[i].unique())
                        st.write("\n","\n")
                        st.write("Value counts for unique categories in ",i,"column:")
                        st.write(df[i].value_counts())

                        st.markdown("**-------------------------------------------------------------------------------------------------**")


