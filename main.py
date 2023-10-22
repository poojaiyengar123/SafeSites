import numpy as np
import streamlit as st
# import matplotlib.pyplot as plt
import pandas as pd
import pydeck as pdk
from PIL import Image
import requests
# from bs4 import BeautifulSoup
import re
import datetime

logo = Image.open("logo.png")
col1, col2, col3 = st.columns(3)
with col2:
    st.image(logo)

data = pd.read_csv("crime_data_by_county_edited.csv")

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
            get_radius=100000,
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
        children = int(st.number_input("Number of Children", min_value=0, step=1))
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
        endBudget = st.number_input("Upper Bound of Budget", min_value=0, step=100, max_value=1000000, value=1000000)
except:
    pass

#submit button
query = {} #dictionary with all the information inputed by user
if st.button("Search", type="primary"):
    query.update([('state', state_chosen), ('county', county_chosen), ('num_of_adults', adults), ('num_of_children', children), ('num_of_infants', infants), ('num_of_pets', pets), ('baths', numOfBaths), ('beds', numOfBeds), ('budget_lower', startBudget), ('budget_upper', endBudget), ('check_in', start_date), ('check_out', end_date)])


check_in_date = query.get("check_in").strftime("%Y-%m-%d")
check_out_date = query.get("check_out").strftime("%Y-%m-%d")
county = query.get("county").replace(" ", "-")
        
state_codes = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'Washington D.C.',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}
state = state_codes.get(query.get("state")).replace(" ", "-")

URL = f"https://www.airbnb.com/s/{county}--{state}/homes?adults={query.get('num_of_adults')}&children={query.get('num_of_children')}&infants={query.get('num_of_infants')}&pets={query.get('num_of_pets')}&price_min={query.get('budget_lower')}&price_max={query.get('budget_upper')}&checkin={check_in_date}&checkout={check_out_date}"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="lxq01kf l1tup9az dir dir-ltr")
list_of_places = []
for result in results:
    text_info = result.find("div", class_="g1qv1ctd c1v0rf5q dir dir-ltr")
    title = text_info.find("div", class_="t1jojoys dir dir-ltr")
    desc = text_info.find("span", class_="t6mzqp7 dir dir-ltr")
    beds = text_info.find("span", class_="dir dir-ltr")

    price_div = text_info.find("div", class_="_i5duul")
    if(text_info.find("span", class_="_tyxjp1") == None):
        price = price_div.find("span", class_="_tyxjp1")
    else:
        price = price_div.find("span", class_="_1y74zjx")
    ratings = text_info.find("span", class_="r1dxllyb dir dir-ltr")

    image_div = result.find("div", class_="m1v28t5c dir dir-ltr")
    image = image_div.find("img", class_="itu7ddv i1mla2as i1cqnm0r dir dir-ltr")
    
    # print(image.get('src'))
    # print(title.text)
    # print(desc.text)
    # print(beds.text)
    # print(re.search("\$\d{1,3}(?:,\d{3})*\s*total", price_div.text).group() +" before tax")
    # if (ratings != None):
    #     print(ratings.text)

    price_print = re.search("\$\d{1,3}(?:,\d{3})*\s*total", price_div.text).group() +" before tax"
    list_of_places.append([image.get('src'), title.text, desc.text, beds.text, price_print])
    if(ratings != None):
        list_of_places[-1].append(ratings.text)
    print()


#printing each listing
# listings = pd.read

# for place in list_of_places:
#     for item in place:
#         print(item)
#     print()


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
