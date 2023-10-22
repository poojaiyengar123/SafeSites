import csv as csv
import streamlit as st
# import matplotlib.pyplot as plt
import pandas as pd
import pydeck as pdk

data = pd.read_csv("crime_data_by_county_edited.csv")
print(data)
# st.line_chart(data)
df = pd.DataFrame(data)
st.pydeck_chart(pdk.Deck(
    map_style=None, 
    initial_view_state=pdk.ViewState(
        latitude=39.83, 
        longitude=-98.58,
        zoom=3,
        pitch=50,
    ), 
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        )
    ],
))

stateCol, countyCol = st.columns(2)
with stateCol: 
    #choosing a state
    stateList = []
    for i, row in data.iterrows():
        try :
            stateList.index(row[1])
        except:
            stateList.append(row[1])
    stateList.sort()
    stateChosen = st.selectbox("State", stateList)

with countyCol:
    #choosing a county
    countyList = []
    for i, row in data.iterrows():
        try :
            if row[1].__eq__(stateChosen): 
                countyList.append(row[0])
        except:
            pass
    countyList.sort()

    try:
        countyChosen = st.selectbox("County", countyList)
    except:
        pass

#number of people on the property
adultCol, childCol, infantCol, petCol = st.columns(4)
with adultCol:
    try:
        adults = int(st.number_input("Number of Adults", min_value=1, step=1))
    except:
        pass

with childCol:
    try:
        children = int(st.number_input("Number of Children", min_value=1, step=1))
    except:
        pass

with infantCol:
    try:
        infants = int(st.number_input("Number of Infants", min_value=0, step=1))
    except:
        pass

with petCol:
    try:
        pets = int(st.number_input("Number of Pets", min_value=0, step=1))
    except:
        pass

#number of beds & baths required
bedCol, bathCol = st.columns(2)
with bedCol:
    numOfBeds = int(st.number_input("Number of Beds", min_value=1, step=1))
with bathCol:
    numOfBaths = int(st.number_input("Number of Baths", min_value=1, step=1))

#dates
date1, date2 = st.columns(2)

with date1: 
    try: 
        startDate = st.date_input("Check-in Date", "today")
    except:
        pass
with date2:
    try:
        endDate = st.date_input("Check-out Date", "today")
    except:
        pass

#budget
lowerBud, upperBud = st.columns(2)
try: 
    with lowerBud:
        startBudget = st.number_input("Lower Bound of Budget", min_value=0, step=100)
    with upperBud: 
        endBudget = st.number_input("Upper Bound of Budget", min_value=0, step=100)
    startBudget, endBudget = st.slider("Range of Budget", value=[0, 1000000])
except:
    pass


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
