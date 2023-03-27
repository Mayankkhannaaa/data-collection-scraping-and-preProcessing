from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(
    '/Users/mayankkhanna/Downloads/chromedriver_mac_arm64/chromedriver.exe')

driver.get('https://amzn.eu/d/5U8V610')
# driver.get('https://amzn.eu/d/gE075d3')

price = driver.find_element(By.XPATH, '//span[@class="a-offscreen"]')
category = driver.find_element(By.ID, "wayfinding-breadcrumbs_feature_div")
# print(driver.find_element(By.XPATH, '//span[@class="a-price-whole"]'))
print(price.get_attribute("innerHTML"))

ul_element = category.find_element(By.CLASS_NAME, "a-unordered-list")

# Find all the link elements
link_elements = ul_element.find_elements(By.TAG_NAME, "a")

# Loop through the link elements and print their text content
link_text = []
for link in link_elements:
    text = link.text.strip()
    if text:
        link_text.append(text)
result = ";".join(link_text)
print(result)


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

except:
    print("")

try:
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
except:
    print("")


avgRating = driver.find_element(By.XPATH, '//span[@class="a-icon-alt"]')
print(avgRating.get_attribute("innerHTML"))

reviewCountParent = driver.find_element(By.XPATH, "//div[contains(@class, 'a-row')][contains(@class, 'a-spacing-medium')][contains(@class, 'averageStarRatingNumerical')]")
reviewCount = reviewCountParent.find_element(By.TAG_NAME, "span")
rating_string = reviewCount.get_attribute("innerHTML")
print(rating_string)
# rating_pattern = r'\b\d{1,3}(?:,\d{3})*\b'
# match = re.search(rating_pattern, rating_string)
# if match:
#     rating_value = match.group(0)
#     print(rating_value)
# else:
#     print("No rating found.")

driver.close()
