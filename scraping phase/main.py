from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.airbnb.com/")

driver.implicitly_wait(10)


# Gets the navigation component, title, and icons
def get_navigation():
    navs = driver.find_elements(By.CLASS_NAME, "c8gkmzg")
    for nav in navs:
        title = nav.find_element(By.CLASS_NAME, "t1h65ots")
        icon = nav.find_element(By.CLASS_NAME, "i1wps9q8")

        nav.click()  # click to get the nav data

        card_data = extract_listings()
        print("title :", title.text)

        for card in card_data:
            print("location ", card['location'])
            print("link ", card['link'])
            print("detail ", card['detail'])
            print("image ", card['image'])

        print()
        print("============================")


# This functions extracts card information from current page
def extract_listings():
    cards = driver.find_elements(By.CLASS_NAME, "cy5jw6o")

    cards_data = []
    for card in cards:
        link_component = card.find_element(By.CLASS_NAME, "bn2bl2p")
        location = card.find_element(By.CLASS_NAME, "t1jojoys")
        date = card.find_element(By.CLASS_NAME, "s1cjsi4j")
        image_component = card.find_element(By.CLASS_NAME, "i1o0kbi8")

        data = {
            "link": link_component.get_attribute("href"),
            "location": location.text,
            "detail": date.text,
            "image": image_component.get_attribute("src")
        }

        cards_data.append(data)

    return cards_data


get_navigation()
