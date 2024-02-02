from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import os
import logging

england_club_url = "https://find.englandfootball.com/"

driver = webdriver.Chrome()
delay = 100

def button_click_to_searching(age):
    # Open the website
    driver.get(england_club_url)
    time.sleep(5)
    
    if len(driver.find_elements(By.ID, "onetrust-accept-btn-handler")) > 0:
        cookies_button = WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        cookies_button.click()

    # Start searching
    searching_button = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "cta_start_searching_now"))
    )
    searching_button.click()
    
    
    search_people_element = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "my_self"))
    )
    search_people_element.click()
    time.sleep(5)
    
    age_input_element = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "selected_age"))
    )
    age_input_element.send_keys(age)
    
    
    next_button_element = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "onboarding_cta_next_question"))
    )
    next_button_element.click()
    
    
    football_button = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "male_football"))
    )
    football_button.click()
    
    next_button_element = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "onboarding_cta_next_question"))
    )
    next_button_element.click()
    
    club_football_button_element = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "club_football"))
    )
    club_football_button_element.click()
    
    all_day_button_element = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "alldays"))
    )
    all_day_button_element.click()
    
    disability_button_element = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "disability_not_sure"))
    )
    disability_button_element.click()
    
    enter_post_code_button = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "enter_postcode"))
    )
    enter_post_code_button.click()
    
    post_code_input = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "searchBox"))
    )
    
    post_code_input.send_keys("England, United Kingdom")
    time.sleep(2)  
    post_code_input.send_keys(Keys.DOWN)
    time.sleep(2)
    
    # Click on the first option in the dropdown
    first_option = WebDriverWait(driver, delay).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "line1"))
    )
    first_option.click()
    
    next_button_element = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "onboarding_cta_next_question"))
    )
    next_button_element.click()
    time.sleep(5)


# current_age = 19
# Configure logging
logging.basicConfig(filename='crawling_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


for current_age in range(35, 76):
    contact_name_result = []
    team_number_result = []
    email_result = []
    telephone_number_result = []
    club_name_result = []
    club_address_result = []
    accredited_to_result = []
    football_type_result = []
    website_result = []
    print("Current age:", current_age)

    # Wait for the button to be clickable
    button_click_to_searching(current_age)
    logging.info("Button Clicked to search done.")
    logging.info(f"Current age: {current_age}")
    
    time.sleep(1)
    
    if len(driver.find_elements(By.ID, "football_recommendations_result_wrapper")) > 0:
        card_divs = WebDriverWait(driver, delay).until(
                    EC.visibility_of_element_located((By.ID, "football_recommendations_result_wrapper"))
                )
        cards = card_divs.find_elements(By.CLASS_NAME, "recommendationCard")
        
        length_of_cards = len(cards)
        
        for card in range(length_of_cards):
            contact_name_result = []
            team_number_result = []
            email_result = []
            telephone_number_result = []
            club_name_result = []
            club_address_result = []
            accredited_to_result = []
            football_type_result = []
            website_result = []
            print(f"OK card {card}")
            logging.info(f"OK card {card}")

            if len(driver.find_elements(By.CLASS_NAME, "css-1gkwtxd")) > 0:
                contact_name_result = []
                team_number_result = []
                email_result = []
                telephone_number_result = []
                club_name_result = []
                club_address_result = []
                accredited_to_result = []
                football_type_result = []
                website_result = []
                
                if len(driver.find_elements(By.ID, f"recommended_football_type_cta_view_maps_of_clubs-{card + 1}")) > 0:
                    football_club_finding = WebDriverWait(driver, delay).until(
                        EC.visibility_of_element_located((By.ID, f"recommended_football_type_cta_view_maps_of_clubs-{card + 1}"))
                    )
                    
                    football_club_finding.click()
                    
                    while True:
                        try:
                            contact_name_result = []
                            team_number_result = []
                            email_result = []
                            telephone_number_result = []
                            club_name_result = []
                            club_address_result = []
                            accredited_to_result = []
                            football_type_result = []
                            website_result = []
                            load_more_element = "map_cta_load_more_recommendations"
                            

                            football_club_load_more = WebDriverWait(driver, 10).until(
                                EC.visibility_of_element_located((By.ID, load_more_element))
                            )
                            
                            time.sleep(0.5)
                            
                            football_club_load_more.click()

                        except TimeoutException:
                            break
                    
                    club_length = "0"

                    # Try to find the element
                    if len(driver.find_elements(By.CLASS_NAME, "css-199032i")) > 0:
                        try:
                            club_length_element = WebDriverWait(driver, delay).until(
                                EC.visibility_of_element_located((By.CLASS_NAME, "css-199032i"))
                            )

                            # Check if the element is found and not empty
                            if club_length_element:
                                # Extract the text content
                                club_length_text = club_length_element.text.strip()
                                # Check if the text content is not empty
                                if club_length_text:
                                    # Split the text and take the first part
                                    club_length = int(club_length_text.split(" ")[0])
                            
                            for club in range(club_length):
                                contact_name_result = []
                                team_number_result = []
                                email_result = []
                                telephone_number_result = []
                                club_name_result = []
                                club_address_result = []
                                accredited_to_result = []
                                football_type_result = []
                                website_result = []
                                
                                more_info_id = f"more_info-{club}"
                                club_provider = f"cta_provider_club_card-{club}"                
                                
                                try:
                                    if len(driver.find_elements(By.ID, club_provider)) > 0:
                                    
                                        club_general_info_button = WebDriverWait(driver, delay).until(
                                            EC.element_to_be_clickable((By.ID, club_provider))
                                        )
                                                        
                                        club_general_info_button.click()
                                        
                                        
                                        action = ActionChains(driver)
                                        
                                        club_info_button = WebDriverWait(driver, delay).until(
                                            EC.element_to_be_clickable((By.ID, more_info_id))
                                        )
                                        
                                        action.key_down(Keys.CONTROL).click(club_info_button).key_up(Keys.CONTROL).perform()  
                                        
                                        if len(driver.window_handles) > 1:
                                            time.sleep(0.5)
                                            driver.switch_to.window(driver.window_handles[1])
                                        else:
                                            action.key_down(Keys.CONTROL).click(club_info_button).key_up(Keys.CONTROL).perform()
                                            time.sleep(3)                    
                                            driver.switch_to.window(driver.window_handles[1])
                                        
                                        club_name = ""
                                        
                                        if len(driver.find_elements(By.ID, "club_name_heading")) > 0:
                                            club_name_element = WebDriverWait(driver, delay).until(
                                                EC.visibility_of_element_located((By.ID, "club_name_heading"))
                                            )
                                                                    
                                            if club_name_element:
                                                club_name = club_name_element.text
                                                
                                                if club_name in club_name_result:
                                                    print("Club already exists, moving to the next club...")
                                                    driver.close()
                                                    driver.switch_to.window(driver.window_handles[0])
                                                    break
                                            else:
                                                club_name = ""
                                        
                                        club_name_result.append(club_name)
                                        
                                        club_address = ""
                                        if len(driver.find_elements(By.CLASS_NAME, "css-86sf1o")) > 0:
                                            club_address_element = WebDriverWait(driver, delay).until(
                                                EC.visibility_of_element_located((By.CLASS_NAME, "css-86sf1o"))
                                            )
                                                                    
                                            if club_address_element:
                                                club_address = club_address_element.text
                                            else:
                                                club_address = ""
                                        
                                        club_address_result.append(club_address)

                                        accredited_to = ""
                                        if len(driver.find_elements(By.CLASS_NAME, "css-o1e1ch")) > 0:
                                            accredited_to_element = WebDriverWait(driver, delay).until(
                                                EC.visibility_of_element_located((By.CLASS_NAME, "css-o1e1ch"))
                                            )
                                                                    
                                            if accredited_to_element:
                                                accredited_to = accredited_to_element.text
                                            else:
                                                accredited_to = ""
                                        
                                        accredited_to_result.append(accredited_to)
                                        
                                        # Find the <ul> element
                                        football_types = []
                                        football_type = ""
                                        if len(driver.find_elements(By.CLASS_NAME, "css-ih6156")) > 0:
                                            football_types_ul_element = WebDriverWait(driver, delay).until(
                                                EC.visibility_of_element_located((By.CLASS_NAME, "css-ih6156"))
                                            )
                                                                    
                                            # Find all <li> elements inside the <ul> tag
                                            football_types_li_elements = football_types_ul_element.find_elements(By.TAG_NAME, "li")
                                            
                                            football_types = [li.text.strip() for li in football_types_li_elements if li.text.strip()]
                                            football_type = ", ".join(football_types)
                                        
                                        football_type_result.append(football_type)
                                        
                                        team_number = ""
                                        if len(driver.find_elements(By.CLASS_NAME, "css-4682ps")) > 0:
                                            team_number_element = WebDriverWait(driver, delay).until(
                                                EC.visibility_of_element_located((By.CLASS_NAME, "css-4682ps"))
                                            )
                                                                    
                                            team_number_text = team_number_element.text
                                            if team_number_text:
                                                team_number = team_number_text.split(" ")[0] if len(team_number_text) > 0 else "0"
                                                
                                        
                                        team_number_result.append(team_number)
                                        
                                        contact_name = ""
                                        if len(driver.find_elements(By.CLASS_NAME, "css-1gpgbx2")) > 0:                   
                                            contact_name_element = WebDriverWait(driver, delay).until(
                                                EC.visibility_of_element_located((By.CLASS_NAME, "css-1gpgbx2"))
                                            )
                                                                    
                                            if contact_name_element:
                                                contact_name = contact_name_element.text
                                            else:
                                                contact_name = ""
                                        
                                        contact_name_result.append(contact_name)
                                        
                                        email = ""
                                        telephone_number = ""
                                        website = ""
                                        if len(driver.find_elements(By.CLASS_NAME, "css-apgqqs")) > 0:
                                            manager_info_div_element = WebDriverWait(driver, delay).until(
                                                EC.visibility_of_element_located((By.CLASS_NAME, "css-apgqqs"))
                                            )
                                                                    
                                            manager_info_ul = manager_info_div_element.find_element(By.TAG_NAME, "ul")
                                            manager_info = manager_info_ul.text.split("\n")
                                            
                                            for info in manager_info:
                                                if "@" in info and not email:
                                                    email = info
                                                elif info.startswith("0") and not telephone_number:
                                                    telephone_number = info
                                                elif not "@" in info and "." in info and not website:
                                                    website = info
                                            
                                        email_result.append(email)
                                        telephone_number_result.append(telephone_number)
                                        website_result.append(website)
                                        
                                        driver.close()
                                        driver.switch_to.window(driver.window_handles[0])
                                    
                                        data = {
                                            "Club Name": club_name_result,
                                            "Address": club_address_result,
                                            "Accredited To": accredited_to_result,
                                            "Football Types": football_type_result,
                                            "Team Numbers": team_number_result,
                                            "Contact Name": contact_name_result,
                                            "Email": email_result,
                                            "Telephone Number": telephone_number_result,
                                            "Website": website_result,
                                        }

                                        # Convert the dictionary to a DataFrame
                                        new_df = pd.DataFrame(data)
                                        
                                        # Check if the CSV file exists
                                        if os.path.exists("club_data.csv"):
                                            logging.info("Handle CSV file")
                                            existing_df = pd.read_csv("club_data.csv")
                                            combined_df = pd.concat([existing_df, new_df]).drop_duplicates(subset=["Club Name"]).reset_index(drop=True)
                                            combined_df.to_csv("club_data.csv", mode="w" if current_age == 5 and card == 0 else "a", header=False, index=False)
                                        else:
                                            logging.info("Export new csv file")
                                            new_df.to_csv("club_data.csv", index=False)
                                except:
                                    break
                            print("OK club Data")
                            logging.info("OK club Data")
                            
                            df = pd.read_csv("club_data.csv")
                            df = df.drop_duplicates(subset=["Club Name"]).reset_index(drop=True)
                            df = df.dropna(how="all")
                            df.to_csv("new_club_data.csv", index=False)
                            driver.back()
                        except:
                            break
                    # Remove Duplicated Data and nan data
                    logging.info("Remove Duplicated Data and nan data")
                    df = pd.read_csv("club_data.csv")
                    df = df.dropna(how="all")
                    df = df.drop_duplicates(subset=["Club Name"]).reset_index(drop=True)
                    df.to_csv("new_club_data.csv")
        # current_age += 1
        # print("Current age incremented to:", current_age)


    # df = pd.read_csv("club_data.csv")
    # df = df.drop_duplicates(subset=["Club Name"]).reset_index()
    # df.to_csv("new_club_data.csv")