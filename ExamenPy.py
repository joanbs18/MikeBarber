import requests
from bs4 import BeautifulSoup 
import mechanize
import builtwith
from wappalyzer import Wappalyzer

wappalyzer = Wappalyzer.latest()


url = "https://asterioargabogados.netlify.app/"

r = requests.get(url)
html_contents = r.text

browser = mechanize.Browser()

browser.open("https://asterioargabogados.netlify.app/")

print(browser.title())
print(browser.response().read())
html_soup = BeautifulSoup(html_contents, 'html.parser')



result = builtwith.builtwith(url)
print("-----------------------------------------------------------")

browser.select_form(name="contact")
browser["name"] = "Jose Adrian"
browser["number"] = "ffff"
browser["email"] = "Joseadrian@gmail.com"
browser["message"] = "Holaaa"
response = browser.submit() 
print(response.read())  


print("-----------------------------------------------------------")


etiquetasEnlace = html_soup.find_all('a')

apps = wappalyzer.analyze(url)

for app in apps:
    print(app)

print(etiquetasEnlace)