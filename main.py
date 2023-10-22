import csv as csv
import streamlit as st
# import matplotlib.pyplot as plt
import pandas as pd
import pydeck as pdk

data = pd.read_csv("crime_data_by_county_edited.csv")
print(data)
# st.line_chart(data)
df = pd.DataFrame(data)
st.pydeck_chart(pdk.Deck(map_style=None, initial_view_state=pdk.ViewState(latitude=39.83, longitude=-98.58,zoom=11,pitch=50,), layers=[],))


# data = pd.read_csv("crime_data_by_county_edited.csv")

# def toString(list):
#     print(list)
#     str = ""
#     for i, row in data.iterrows():
#         str += row[i]

# #choosing a state
# stateList = []
# for i, row in data.iterrows():
#     try :
#         stateList.index(row[1])
#     except:
#         stateList.append(row)

# stateChosen = st.radio("State", stateList)

# #choosing a county
# countyList = []
# for i, row in data.iterrows():
#     try :
#         row.index(stateChosen)
#         #if doesn't throw exception, it has the state
#         countyList.append(row[0])
#     except:
#         pass

# countyChosen = st.radio("County", countyList)

# #number of people on the property
# numOfPeople = st.number_input("Number of Guests")
# #number of bedrooms required
# numOfBeds = st.number_input("Number of Beds")

# #dates
# startDate = st.date_input("Starting Date", "today")
# endDate = st.date_input("End Date", "today")

# #budget
# startBudget, endBudget = st.slider("Range of budget", value=[0, 1000000])

# #pet
# pet = st.slider("Pets", value=[0, 10])

# import pandas as pd
# import streamlit as st
# # import matplotlib.pyplot as plt

# data = pd.read_csv("crime_data_by_county_edited.csv")
# print(data)




# # create 2 new columns:
#     # county name
#     # state name
# # create 1 new column: combined index of all numbers in provided columns
# # use streamlit and pandas to display data nicely
# # pip install streamlit
# # pip install matplotlib.pyplot
# # formula for crime index : (violent crime + property crime) / 100,000
