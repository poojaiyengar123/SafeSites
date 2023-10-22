import requests
from bs4 import BeautifulSoup
import re
import datetime

# full block = lxq01kf l1tup9az dir dir-ltr
# text info class = g1qv1ctd c1v0rf5q dir dir-ltr
# title class = t1jojoys dir dir-ltr
# info blocks class = fb4nyux s1cjsi4j dir dir-ltr
# beds class = 
# price class = a8jt5op dir dir-ltr
# image div = m1v28t5c dir dir-ltr
# image class = itu7ddv i1mla2as i1cqnm0r dir dir-ltr
# ratings class = r1dxllyb dir dir-ltr

query = {}
query.update([('state', 'NJ'), ('county', 'South Brunswick'), ('num_of_adults', 1), ('num_of_children', 2), ('num_of_infants', 0), ('num_of_pets', 1), ('baths', None), ('beds', None), ('budget_lower', 50), ('budget_upper', 1000), ('check_in', datetime.date(2023, 10, 22)), ('check_out', datetime.date(2023, 10, 24))])

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

# for place in list_of_places:
#     for item in place:
#         print(item)
#     print()
