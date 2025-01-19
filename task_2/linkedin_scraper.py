from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import csv
from random import randint
from collections import Counter

class LinkedInProfileCrawler:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = self.setup_driver()
        
    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return webdriver.Chrome(options=chrome_options)
        
    def login(self):
        try:
            self.driver.get('https://www.linkedin.com/login')
            time.sleep(2)
            
            # Login
            self.driver.find_element(By.ID, "username").send_keys(self.email)
            self.driver.find_element(By.ID, "password").send_keys(self.password)
            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(5)
            return True
            
        except Exception as e:
            print(f"Login failed: {e}")
            return False
            
    def get_profile_data(self, profile_url):
        try:
            print(f"Accessing profile: {profile_url}")
            self.driver.get(profile_url)
            time.sleep(5)
            
            # Get name from profile URL if scraping fails
            profile_name = profile_url.split('/in/')[-1].strip('/').replace('-', ' ').title()
            
            # Progressive scroll
            for i in range(3):
                self.driver.execute_script(f"window.scrollTo(0, {i * 500});")
                time.sleep(1)
            
            wait = WebDriverWait(self.driver, 10)
            
            # Try to get actual name from page, fallback to URL-derived name
            try:
                name = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "h1.text-heading-xlarge")
                )).text.strip()
            except:
                name = profile_name
                
            # Get job title and extract company if present
            job_title = "N/A"
            company = "N/A"
            
            try:
                headline = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.text-body-medium")
                )).text.strip()
                
                if " at " in headline:
                    job_title, company = headline.split(" at ", 1)
                else:
                    job_title = headline
                    try:
                        company = self.driver.find_element(
                            By.CSS_SELECTOR, 
                            "div.experience-group-header__company, .pv-entity__secondary-title"
                        ).text.strip()
                    except:
                        pass
                        
            except Exception as e:
                print(f"Error extracting headline: {e}")
            
            print(f"Successfully scraped: {name} | {job_title} | {company}")
            return {
                'name': name,
                'job_title': job_title,
                'company': company
            }
            
        except Exception as e:
            print(f"Error extracting profile data: {e}")
            return {'name': profile_name, 'job_title': 'N/A', 'company': 'N/A'}

    def search_profiles(self, search_url, max_profiles=10):
        try:
            print(f"Searching first page at: {search_url}")
            self.driver.get(search_url)
            time.sleep(5)
            
            profiles = []
            for _ in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            
            search_results = self.driver.find_elements(
                By.CSS_SELECTOR, 
                "div.search-results-container li.reusable-search__result-container"
            )
            print(f"Found {len(search_results)} results on page")
            
            for result in search_results[:max_profiles]:
                try:
                    main_link = result.find_element(
                        By.CSS_SELECTOR, 
                        "span.entity-result__title-text a"
                    )
                    profile_url = main_link.get_attribute('href')
                    
                    if '/in/' not in profile_url:
                        continue
                    
                    name = main_link.text.strip()
                    if not name or name == "LinkedIn Member":
                        name = profile_url.split('/in/')[-1].strip('/').replace('-', ' ').title()
                    
                    try:
                        title = result.find_element(
                            By.CSS_SELECTOR,
                            "div.entity-result__primary-subtitle"
                        ).text.strip()
                    except:
                        title = "N/A"
                        
                    try:
                        location = result.find_element(
                            By.CSS_SELECTOR,
                            "div.entity-result__secondary-subtitle"
                        ).text.strip()
                    except:
                        location = "N/A"
                    
                    profiles.append({
                        'url': profile_url,
                        'name': name,
                        'preview_title': title,
                        'location': location
                    })
                    print(f"Found profile: {name} | {title} | {location}")
                    
                except Exception as e:
                    print(f"Error processing result: {e}")
                    continue
            
            print(f"Successfully found {len(profiles)} valid profiles")
            return profiles
            
        except Exception as e:
            print(f"Error in search: {e}")
            return []

    def close(self):
        self.driver.quit()

def main():
    crawler = LinkedInProfileCrawler(
        email='your_linkedin_connected_mail',
        password='its_passsword'
    )
    
    if crawler.login():
        # List of examples IIT graduate profiles 
        # iit_profiles = [
        #     "https://www.linkedin.com/in/pushpforgbe/",
        #     "https://www.linkedin.com/in/vinaykumariitr/",
        #     "https://www.linkedin.com/in/ronak-malav-iit-r-413400202/",
        # ]
        iit_profiles = [
            "https://www.linkedin.com/in/example1/",
            "https://www.linkedin.com/in/example2/"
        ]
        
        scraped_data = []
        for profile_url in iit_profiles:
            try:
                data = crawler.get_profile_data(profile_url)
                scraped_data.append(data)
                print(f"Scraped {len(scraped_data)}/{len(iit_profiles)} profiles")
                time.sleep(randint(3, 7))  # Random delay between requests
            except Exception as e:
                print(f"Error processing {profile_url}: {e}")
            
        if scraped_data:
            with open("iit_alumni_data.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=['name', 'job_title', 'company'])
                writer.writeheader()
                writer.writerows(scraped_data)
                print(f"Successfully saved {len(scraped_data)} profiles to CSV")
        else:
            print("No valid profiles were scraped")
            
    crawler.close()

if __name__ == "__main__":
    main()
