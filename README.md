# Data Collection Pipeline

# Milestone 3 
I chose to use the web site Indeed for this webscraping project as I aspire to be a Data Engineer. With this project I will be able to collect data and review the best jobs in market, comparing data such as, salary, benefits. 

In the code below I used selenium to navigate through the webpages of the website until I reach and collect the weblinks of the product pages. I used several methods to do this:

Close the login pop up box upon running the website.
Navigate to each section of the website, and collect URLs on the web page. 

The core of the project is the development of a data scraping tool. The Selenium python package is used to control the Chrome browser via ChromeDriver. Selenium provides direct control over the browser, allowing the scraper to click on dropdown menus and navigate to pages.

The data scraping tool is created as a class, and all of the functions for each step of the process are then created as methods of the class.

Selenium is used to navigate to the various fields on the search page and complete them using our initial paramters. Different approaches are required depending on whether the fields are free text input or menu dropdowns.
The method stores the search results URL as an attribute of the class, and then returns.

