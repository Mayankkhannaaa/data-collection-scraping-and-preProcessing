from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import re

driver = webdriver.Chrome(
    '/Users/mayankkhanna/Downloads/chromedriver_mac_arm64/chromedriver.exe')

filename = "my_table.csv"
column_name = "amazon-ids"
count=0

# Open the CSV file for reading
with open(filename, "r") as file:
    reader = csv.DictReader(file)

    # Loop over each row in the CSV file
    for row in reader:
        # Extract the value in the specified column
        value = row[column_name]
        count += 1
        url = "https://www.amazon.in/dp/{value}/"
        formatted_url = url.format(value=value)
        driver.get(formatted_url)
        # driver.get('https://amzn.eu/d/gE075d3')

        newDataRow=[]
        flagForFeature=True
        try:
            price = driver.find_element(By.XPATH, '//span[@class="a-offscreen"]')
            priceValue=price.get_attribute("innerHTML")
            print(priceValue)
            newDataRow.append(priceValue)
        except:
            newDataRow.append(0)
            print("")

        try:
            category = driver.find_element(By.ID, "wayfinding-breadcrumbs_feature_div")
            # print(driver.find_element(By.XPATH, '//span[@class="a-price-whole"]'))
            ul_element = category.find_element(By.CLASS_NAME, "a-unordered-list")

            #   Find all the link elements
            link_elements = ul_element.find_elements(By.TAG_NAME, "a")

            # Loop through the link elements and print their text content
            link_text = []
            for link in link_elements:
                text = link.text.strip()
                if text:
                    link_text.append(text)
            result = ";".join(link_text)
            print(result)
            newDataRow.append(result)
        except:
            newDataRow.append("")
            print("")


        try:
            features = driver.find_element(By.XPATH, "//table[contains(@class, 'a-normal')][contains(@class, 'a-spacing-micro')]")
            features1 = features.find_elements(By.TAG_NAME, "td")
            # print(features1.get_attribute("innerHTML"))
            featuresJson=[]
            for link1 in features1:
                text = link1.text.strip()
                if text:
                    featuresJson.append(text)

            json_data = {}
            for i in range(0, len(featuresJson), 2):
                key = featuresJson[i]
                value = featuresJson[i+1]
                json_data[key] = value
            print(json_data)
            newDataRow.append(json_data)
        except:
            flagForFeature=False
            print("")

        try:
            if(not flagForFeature):
                featuresOther = driver.find_element(By.ID,"detailBullets_feature_div")
                featuresOtherOpened = featuresOther.find_elements(By.TAG_NAME, "li")

                otherFeaturesJson=[]
                for link1 in featuresOtherOpened:
                    text = link1.text.strip()
                    if text:
                        newArr = text.split(":")
                        for item in newArr:
                            text1= item.strip()
                            if text1:
                                otherFeaturesJson.append(text1)

                other_json_data = {}
                for i in range(0, len(otherFeaturesJson), 2):
                    key = otherFeaturesJson[i]
                    value = otherFeaturesJson[i+1]
                    other_json_data[key] = value
                print(other_json_data)
                newDataRow.append(other_json_data)
        except:
            print("")


        try:
            avgRating = driver.find_element(By.XPATH, '//span[@class="a-icon-alt"]')
            ratingNum=avgRating.get_attribute("innerHTML")
            print(ratingNum)
            newDataRow.append(ratingNum)
        except:
            newDataRow.append(0)

        try:

            reviewCountParent = driver.find_element(By.XPATH, "//div[contains(@class, 'a-row')][contains(@class, 'a-spacing-medium')][contains(@class, 'averageStarRatingNumerical')]")
            reviewCount = reviewCountParent.find_element(By.TAG_NAME, "span")
            rating_string = reviewCount.get_attribute("innerHTML")
            new_string = rating_string[77:]
            new_string.strip()
            match = re.search(r'\d+', new_string)
            if match:
                rating = int(match.group())
                print(rating)
            else:
                print("No rating found in the string.")
            newDataRow.append(rating)
        except:
            newDataRow.append(0)

        # Load existing table from CSV file
        with open("my_table.csv", "r") as file:
            reader = csv.reader(file)
            table = list(reader)

        # Add new rows to the table
        new_rows = [newDataRow]
        table += new_rows

        # Save the updated table to the CSV file
        with open("my_table.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(table)

        print("Table updated and saved to my_table.csv")

        flagForFeature=True

        driver.close()

        # Break the loop if we've processed 1000 rows
        if count == 1000:
            break
        # Do something with the value, e.g. print it
        print(value)
