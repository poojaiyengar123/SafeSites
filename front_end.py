import streamlit as st
import pandas as pd

data = pd.read_csv("crime_data_by_county_edited.csv")

#choosing a state
stateList = []
for i, row in data.iterrows():
    try :
        stateList.index(row[1])
    except:
        stateList.append(row[1])

stateChosen = st.radio("State", stateList)

#choosing a county
countyList = []
for i, col in data.iterrows():
    try :
        data[r].index(stateChosen)
        #if doesn't throw exception, it has the state
        countyList.append(data[i][col])
        print(countyList)
    except:
        pass

try:
    countyChosen = st.radio("County", countyList)
except:
    pass


#number of people on the property
numOfPeople = int(st.number_input("Number of Guests"))
#number of bedrooms required
numOfBeds = int(st.number_input("Number of Beds"))

#dates
try: 
    startDate = st.date_input("Starting Date", "today")
except:
    pass

try:
    endDate = st.date_input("End Date", "today")
except:
    pass

#budget
try: 
    startBudget = int(st.number_input("Lower Bound of Budget"))
    endBudget = int(st.number_input("Upper Bound of Budget"))
    startBudget, endBudget = st.slider("Range of budget", value=[0, 1000000])
except:
    pass

#pet
try: 
    pet = st.slider("Pets", value=[0, 10])
except:
    pass

