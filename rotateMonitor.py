###IMPORTS 
import requests
import csv
from io import StringIO
import time
import rotatescreen

#background process to scan csv file from webserver and rotate screen according to 
#given gyroscope values
while True:
# The URL of the CSV file
    url = 'http://10.37.61.126:8000/output.csv'
    screen = rotatescreen.get_primary_display()
# Fetch the content
    response = requests.get(url)    
    response.raise_for_status()  # Raise an error for HTTP failures

# Use StringIO to convert the content into a file-like object so it can be read into a csv.reader
    csv_data = StringIO(response.text)

# Read the CSV data
    reader = csv.reader(csv_data, delimiter=',')


    for row in reader:
        if(float(row[0]) > 50 and float(row[1]) < 10 and float(row[1]) > -10):
            screen.set_landscape()
        else:
            screen.set_portrait_flipped()
    time.sleep(1)
