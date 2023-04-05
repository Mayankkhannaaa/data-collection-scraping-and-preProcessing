# Scraping Amazon Product Data 🗂️

This project uses the `@scrapingant/amazon-proxy-scraper` npm package to scrape data from Amazon product pages.

## Usage 💻

To use this project and get the most out of it:

1. Install the required npm package by running `npm i @scrapingant/amazon-proxy-scraper`.
2. Run the `script.js` file using Node.js by runnig command `node script.js`.
3. If you face problems while running the API, make sure you are under the API calls limit. If not so, create a new account and change the old API with the new one.
4. The CSV files with the scraped data will be automatically generated and saved.
5. Add the changes to your Git repository using `git add .`.
6. Commit the changes using `git commit -m "message"`.
7. Push the changes to your remote repository using `git push`.

## Scraping Amazon Product Data Using WebDriver 🗂️

The installation process is given here `https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a`

## Run the Script 💻

Use command `python {fileName.py}` to run the script

## Usage WebDriver 💻

To use this project and get the most out of it:

1. Run `csvCreation.py` to create the table

**Note that you have to replace webDriver location and put the location of where it is installed on your computer
**Also, replace the name of the csv file you have the ASIN numbers in.
2. Run `webDriverScript.py` to extract the data
3. And you are good to go.

## Preprocessing Data 📊

File to be accessed: `cleanMyData.py`

1. All the neccessary factors to preprocess the data and do basic data augmentation is present in the file.
2. Everything is commented with some headlines.
3. Uncomment the part of code to be used.
4. Run the file using `python cleanMydata.py`
**Note, change the dataset file location as desired.

## Create a new pull request ℹ️

1. `git checkout -b my-feature-branch`
2. `git add .`
3. `git commit -m "with your message"`
4. `git push origin my-feature-branch`
5. Go to the forked repo and create a new pull request from the my-feature-branch

## Pull from main repository

1. If not added the main repo as the remote repo, use `git remote add upstream https://github.com/Mayankkhannaaa/data-collection-scraper`
2. `git fetch upstream`
3. `git checkout main`
4. `git merge upstream/main`
5. `git push origin main`

## Pull the merged changes to local main machine

1. `git pull`
