import unittest
import HtmlTestRunner

from proiect import Login_page
from proiect import Dashboard
from proiect import Search_button
from proiect import Menu_aplication

class TestSuite(unittest.TestCase):

    def test_suite(self):


        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login_page),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dashboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(Search_button),
            unittest.defaultTestLoader.loadTestsFromTestCase(Menu_aplication)

        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True, # vrem sa generam un singur raport cu toate testele
            report_title="Test Execution Report",
            report_name="Raport Proiect final"
        )


        runner.run(teste_de_rulat)
