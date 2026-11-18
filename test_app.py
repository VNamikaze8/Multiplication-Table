
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5001")

    number = driver.find_element(By.ID, "number")
    number.send_keys("5")

    driver.find_element(By.ID, "generate").click()

    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )

    rows = driver.find_elements(By.CSS_SELECTOR, "#table li")

    assert result.text == "Table of 5"
    assert len(rows) == 10
    assert rows[0].text == "5 × 1 = 5"
    assert rows[9].text == "5 × 10 = 50"

    print("PASS: Multiplication table generated correctly")
    print("PASS: All 10 rows displayed")
    print("ALL SELENIUM TESTS PASSED")

finally:
    driver.quit()
