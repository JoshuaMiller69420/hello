import random

#ran_num = random.randint(1, 10000)
#random_num_guestion = print(f"Remember this randim number: {ran_num}")
#random_num_guestion.del

#import time
#for x in range (0,5):  
#    b = "Loading" + "." * x
#    print (b, end="\r")
#    time.sleep(1)

import json

# Load the JSON data from a file
with open('high_scores.json', 'r') as file:
    data = json.load(file)

# Sort the data by the "value" key in descending order
#sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)

# Output the sorted data
sorted_data = sorted(data, key=lambda x: x['value'], reverse=True)
for index, cust in enumerate(sorted_data, start=1):
    print(f"{index}. {cust['name']} - {cust['value']}")

# {data, key=lambda(reverse=True)}