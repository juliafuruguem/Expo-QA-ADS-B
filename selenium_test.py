from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class TestGoogleSearch(unittest.TestCase):

    def setUp(self):
        # Inicializa o navegador
        self.driver = webdriver.Chrome()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        
        # Verificar se a página carregou corretamente
        self.assertIn("Google", driver.title)

        # Encontrar o campo de busca e realizar uma pesquisa
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Katalon" + Keys.RETURN)

        # Aguardar até que o resultado apareça e verificar o título da página
        driver.implicitly_wait(10)
        self.assertIn("Katalon", driver.title)

    def tearDown(self):
        # Fechar o navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
