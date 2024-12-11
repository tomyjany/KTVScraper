import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import box
from datetime import date
import yaml
import urllib3

# Suppress only the single InsecureRequestWarning from urllib3 needed for this case
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('cfg.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


from bs4 import BeautifulSoup

# Suppress only the single InsecureRequestWarning from urllib3 needed for this case
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Scraper:
    def __init__(self, custom_username=cfg.USERNAME, custom_password=cfg.PASSWORD, year=date.today().year):
        self.username = custom_username
        self.password = custom_password
        self.year = year
        self.driver = webdriver.Chrome()
        self.connect()
        self.session = self.get_seesion()

        print(year)
    

    def get_seesion(self):
        cookies = self.driver.get_cookies()
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
        
        return session



    def connect(self):
        # Open the login page
        self.driver.get("https://rezervace.ktv.tul.cz")

        # Wait for the page to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Fill in the username and password fields
        self.driver.find_element(By.ID, "frm-signForm-signForm-email").send_keys(cfg.USERNAME)
        password_field = self.driver.find_element(By.ID, "frm-signForm-signForm-password")
        password_field.send_keys(cfg.PASSWORD)

        # Press Enter in the password field
        password_field.send_keys(Keys.RETURN)

        # Wait for the next page to load (adjust timeout as needed)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        print("Login successful!")

        # Wait for login to complete
        time.sleep(2)  # Adjust based on the site's behavior
        self.cookie = self.driver.get_cookies()
    

    def get_url_week(self, week_number):
        """This method will extract data from the url that ends in the number of the week"""
        url = f"https://rezervace.ktv.tul.cz/asc?ascCalendarComponent-year={self.year}&ascCalendarComponent-week={week_number}"
        response = self.session.get(url, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            print("Error")
            print(response.status_code)
            print(response.text)
            return None


    def get_activities_strings(self, week_number):
        """This method will scrape the url that ends in the number of the week"""
        html_content = self.get_url_week(week_number)
        activities = []
        if html_content:
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("div", class_="c-asc-table__sidebar-col")
            for element in elements:
                span = element.find("span")
                if span:
                    activity = span.get_text(strip=True)
                    activities.append(activity)
                    print(span.get_text(strip=True))
        return activities

    def count_logged_in_activities(self, week_number):
        """This method will count how many times the user has logged in for each unique title and save the metadata"""
        html_content = self.get_url_week(week_number)
        login_counts = {}
        if html_content:
            soup = BeautifulSoup(html_content, "html.parser")
            
            # Extract the day of the week and date
            header = soup.find("div", class_="c-asc-table__head")
            if header:
                print("found header: ", header)
                day_info = header.find("div", class_="c-asc-table__sidebar-col").get_text(strip=False)
                print("day_info: ", day_info.strip())
                day_of_week, date = day_info.split(' ', 1)
                day_of_week = day_of_week.strip()
                date = date.strip()
            
            rows = soup.find_all("div", class_="c-asc-table__row")
            for row in rows:
                elements = row.find_all("div", class_="c-asc-table__item--activity")
                for element in elements:
                    span = element.find("span", class_="c-asc-table__info-detail")
                    if span:
                        title = span.get_text(strip=True)
                        if "c-asc-table__item--logged-in" in element['class']:
                            ul = element.find("ul", class_="c-asc-table__list")
                            time_text = ul.find("li").get_text(strip=True) if ul else "N/A"
                            metadata = {
                                "week": week_number,
                                "day_of_week": day_of_week,
                                "date": date,
                                "time": time_text
                            }
                            if title in login_counts:
                                login_counts[title]["count"] += 1
                                login_counts[title]["metadata"].append(metadata)
                            else:
                                login_counts[title] = {
                                    "count": 1,
                                    "metadata": [metadata]
                                }
        return login_counts
    def count_all_activities(self):
        pass
    



if __name__ == "__main__":
    scraper = Scraper()
    print(scraper.count_logged_in_activities(49))



    

