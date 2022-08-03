# import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from time import sleep


driver = webdriver.Chrome("C:\\chromedriver\\chromedriver\\chromedriver.exe")
driver.get("https://www.amazon.com/")

search_box = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
search_box.clear()
search_box.send_keys("Dell laptop")
driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
driver.find_element(By.XPATH, '//span[text()="Dell"]').click()

laptop_names = []
laptop_prices =[]
laptop_reviews = []

all_items = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

for item in all_items:

    name = item.find_elements(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
    for i in name:
        laptop_names.append(i.text)

    try:
        if len(item.find_elements(By.XPATH,".//span[@class='a-price-whole']")) > 0:
            prices = item.find_elements(By.XPATH,".//span[@class='a-price-whole']")
            for i in prices:
                laptop_prices.append(i.text)
        else:
            laptop_prices.append("0")
    except:
        pass        
    try:
        if len(item.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")) > 0 :
            reviews = item.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")
            for i in reviews:
                laptop_reviews.append(i.text)
        else:
            laptop_reviews.append("0")
    except:
        pass

print("Name of laptops ====>", len(laptop_names))
print("Price of laptops ====>", len(laptop_prices))
print("Reviews of laptops ====>", len(laptop_reviews))

# df = pd.DataFrame(zip(laptop_names,laptop_prices,laptop_reviews),columns=['laptop_names', 'laptop_prices', 'laptop_reviews'])
# df.to_excel(r"\excel\amazon\laptop.xlsx",index=False)
