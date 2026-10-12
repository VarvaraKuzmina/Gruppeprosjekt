import csv
import matplotlib.pyplot as plt
import datetime

with open('sinnes_2014_2025.csv', 'r', encoding='utf-8-sig') as file:   #We read the file and use encoding to make sure that norwegian letters in the CSV file are read correctly.
    reader=csv.DictReader(file, delimiter=';')                           #We use `DictReader` to access columns by their names instead of their index numbers. The `delimiter` tells the code that the data is separated by ;

    date=[]
    Nedbør=[]
    
    for row in list(reader)[:-1]:                                          #We use `list(reader)[:-1]` to remove the last row from the CSV file.                        
        if row['Nedbør (døgn)'] != '-':                                           #We start with an `if` statement because we want to exclude all missing values marked with - in the file. To make sure that the date and nedbør lists have the same number of values, we read both columns inside the same condition.
            Nedbør.append(float(row['Nedbør (døgn)'].replace(',', '.')))             #We replace commas with dots to convert the values into the correct numerical format.
            date.append(datetime.datetime.strptime(row['Tid(norsk normaltid)'], '%d.%m.%Y'))     #We use `datetime` to convert the dates from text strings into date objects that python can understand and work with.

    all_data=sorted(zip(date, Nedbør))         #We need to sort the values because a few rows at the end of the file are in the wrong order. First, we combine both columns using `zip` to create matching pairs of dates and precipitation values. Then, we use `sorted` to put them in the correct chronological order.
    date, Nedbør=zip(*all_data)                #We separate the sorted data back into two individual lists.

plt.figure(figsize=(15, 5))
plt.plot(date, Nedbør, linestyle='-', linewidth=1)
plt.show()