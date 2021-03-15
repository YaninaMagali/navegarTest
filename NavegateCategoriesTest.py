import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class NavegateCategoriesTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.mercadolibre.com.ar")

    def test_navegate_categories(self, expected_quantity = 600):
        cat_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Categorías')]")))
        ActionChains(self.driver).move_to_element(cat_option).perform()
        tecno_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "// a[contains(text(), 'Tecnología')]")))
        ActionChains(self.driver).move_to_element(tecno_option).perform()
        tecno_option.click()
        cel_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Celulares y Smartphones')]")))
        cel_option.click()

        cat_title = self.driver.find_element_by_xpath("//span[contains(text(),'Celulares y Teléfonos')]").text
        subcat_title = self.driver.find_element_by_xpath("//h1[contains(text(),'Celulares y Smartphones')]").text
        results = self.driver.find_element_by_xpath("// span[contains(text(), 'resultados')]").text
        results = results.split(" ")[0]

        self.assertEqual(cat_title, "Celulares y Teléfonos", "Error")
        self.assertEqual(subcat_title, "Celulares y Smartphones", "Error")
        self.assertEqual(results, expected_quantity, "Error")

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
