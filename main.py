import pandas as pd
import streamlit as st
# import matplotlib.pyplot as plt

data = pd.read_csv("crime_data_by_county_edited.csv")
print(data)




# create 2 new columns:
    # county name
    # state name
# create 1 new column: combined index of all numbers in provided columns
# use streamlit and pandas to display data nicely
# pip install streamlit
# pip install matplotlib.pyplot
# formula for crime index : (violent crime + property crime) / 100,000
