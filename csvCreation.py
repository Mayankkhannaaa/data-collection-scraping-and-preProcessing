import csv

table = [["Price", "Category", "Features","AvgRating","TotalRatings"]]

# Save the table to a CSV file
with open("my_table.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(table)

print("Table saved to my_table.csv")