import declarations as d

for i in range(9):
    driver = d.driver.get(d.websites[0])
    extract_data(driver)

def extract_data(driver):
