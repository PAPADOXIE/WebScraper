from selenium import webdriver as wd
from bs4 import BeautifulSoup as b4
import pandas as pd

driver = wd.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
websites = [9]
websites[0] = 'https://ctftime.org/'