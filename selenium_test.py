from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

class AppDynamicsJob(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary = "/usr/bin/firefox"  # Defina o caminho correto para o binário do Firefox, se necessário
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://example.com")  # Substitua pelo URL que deseja testar

    def test_app_dynamics_job(self):
        # Seu código de teste vai aqui
        self.assertIn("Example Domain", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
