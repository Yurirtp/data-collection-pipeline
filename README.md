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

# def extract_data(self):
            self.get_web_page()
            self.accept_cookies()
            self.find_search_bar()
            self.search_input()
            self.scroll_page_down()

            
            for key, value in data.items():
                data = {}
                print(key, ':', value)
                job_info = {}
                job_info['job_title'] = 'Junior Software Engineer'  # Extract the job title
                job_info['company'] = 'Hatch'  # Extract the company name
                job_info['location'] = 'Birmingham'  # Extract the location
                job_info['salary'] = '£42,000 a year'  # Extract the salary
                job_info['employment_type'] = 'Full-time'  # Extract the employment type
                job_info['benefits'] = ['Company pension']  # Extract the benefits
                self.date = str(date.today())
                self.hour = datetime.now()
                self.current_time = str(self.hour.strftime("%H:%M"))
                data['job_info'] = job_info  # Add the job information to the data dictionary

                for key, value in data.items():
                    print(key, ':', value)
                        data[job_id] = {
                        'job_title': job_title,
                            'company': company,
                            'location': location,
                            'salary': salary,
                            'employment_type': employment_type,
                            'benefits': benefits
                        }
                        # ## https://www.youtube.com/watch?v=HpLJEGApKEs