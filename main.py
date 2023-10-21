import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

data = pd.read_csv("crime_data_by_county_us.csv")
display(data)



# create a new column in the table with combined index of all numbers in provided columns
# use streamlit and pandas to display data nicely
# pip install streamlit
# pip install matplotlib.pyplot
# formula for crime index : (violent crime + property crime) / 100,000