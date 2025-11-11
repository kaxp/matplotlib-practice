import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

##! First way of import the data and working with it using csv library
# with open("lib/data/languages.csv") as csv_file:
#     # Save as dictionary so that we can access the data using Key and not jsut index
#     csv_reader = csv.DictReader(csv_file)

#     # # Get the first row of data
#     # row = next(csv_reader)

#     # print(row) # {'Responder_id': '1', 'LanguagesWorkedWith': 'HTML/CSS;Java;JavaScript;Python'}

#     # print(row['LanguagesWorkedWith']) # HTML/CSS;Java;JavaScript;Python

#     # # This above data is not clean, we can make it list of languages
#     # print(row['LanguagesWorkedWith'].split(';')) # ['HTML/CSS', 'Java', 'JavaScript', 'Python']

#     #? Now since we want to display the most popular 15 langauges for this task we will 
#     #? add them to Counter. 
#     language_counter = Counter()

#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))

##! Another recommended way of import the data and working with it using pandas
data = pd.read_csv("lib/data/languages.csv")
ids = data['Responder_id']

lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = [] # x-axis
popularity = [] # y-axis

# return a list of tuple of length 15, in our csv we have 28 languages but these are 15 most common
print(language_counter.most_common(15))
#[('JavaScript', 59219), ('HTML/CSS', 55466), ('SQL', 47544), ('Python', 36443), ('Java', 35917), ('Bash/Shell/PowerShell', 31991), ('C#', 27097), 
# ('PHP', 23030), ('C++', 20524), ('TypeScript', 18523), ('C', 18017), ('Other(s):', 7920), ('Ruby', 7331), ('Go', 7201), ('Assembly', 5833)]

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# To display the most popular at start of graph 
languages.reverse()
popularity.reverse() 

# using barh (horizontal bar as there are lot of data overlapping)
plt.barh(languages, popularity)
plt.title("Most popular languages")
plt.xlabel("Number of people who use it")

plt.tight_layout()

plt.show()



