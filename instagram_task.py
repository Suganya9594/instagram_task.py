import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Load environment variables from .env file
load_dotenv()

# Get username and password from environment variables
USERNAME = os.getenv('INSTAGRAM_USERNAME')
PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

# Initialize the WebDriver
driver = webdriver.Chrome()

# Function to log in to Instagram
def login(username, password):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)  # Wait for the login page to load

    # Find username and password fields and enter credentials
    user_input = driver.find_element(By.NAME, 'username')
    pass_input = driver.find_element(By.NAME, 'password')

    user_input.send_keys(username)
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for the login to complete

# Function to get followers and following counts
def get_counts(profile_username):
    driver.get(f'https://www.instagram.com/{profile_username}/')
    time.sleep(2)  # Wait for the profile page to load

    # Fetch followers count
    try:
        followers_element = driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]")
        followers_count = followers_element.text  # This will get '190K followers'

        # Fetch following count
        following_element = driver.find_element(By.XPATH, "//a[contains(@href, '/following')]")
        following_count = following_element.text  # This will get '7 following'

        # If you want just the numbers
        following_number = driver.find_element(By.XPATH, "//a[contains(@href, '/following')]//span[contains(@class, 'html-span')]").text
        
        # Print the results
        print(f"Followers: {followers_count}")
        print(f"Following: {following_number}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Log in to Instagram using credentials from the .env file
login(USERNAME, PASSWORD)

# Replace 'target_username' with the Instagram username you want to inspect
get_counts('guviofficial')

# Close the driver
driver.quit()

