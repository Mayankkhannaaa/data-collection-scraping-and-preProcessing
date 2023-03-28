import csv

filename = "my_table.csv"
column_name = "Price"

# Open the CSV file for reading
with open(filename, "r") as file:
    reader = csv.DictReader(file)

    # Loop over each row in the CSV file
    for row in reader:
        # Extract the value in the specified column
        value = row[column_name]

        # Do something with the value, e.g. print it
        print(value)