# Importing the necessary modules
import csv
import random
import time

# Initializing variables
x_value = 0
total_1 = 1000
total_2 = 1000
fieldnames = ["x_value", "total_1", "total_2"]

# Creating and writing the header to the CSV file
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

# Infinite loop to continuously generate and write data to the CSV file
while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Creating a dictionary with the data to be written
        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }
        
        # Writing the data to the CSV file
        csv_writer.writerow(info)
        
        # Printing the values for debugging purposes
        print(x_value, total_1, total_2)
        
        # Updating the variables for the next iteration
        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)
    
    # Pausing the execution for 1 second before the next iteration
    time.sleep(1)
