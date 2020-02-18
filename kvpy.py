import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
browser = webdriver.Chrome(chrome_options=options)
roll = input()
m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
d = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
years = ['2001', '2000', '2002']
for year in years:
	for i in m:
		for j in d:
			browser.get(r"http://kvpy.iisc.ernet.in/kvpy1718/checkMarks.php")
			rollno = browser.find_element_by_name("id")
			rollno.send_keys(roll)
			day =  browser.find_element_by_name("dd")
			month =  browser.find_element_by_name("mm")
			yearyyyy =  browser.find_element_by_name("yyyy")
			day.send_keys(j)
			month.send_keys(i)
			yearyyyy.send_keys(year)
			print(j, "-", i,"-", year)
			submit = browser.find_element_by_xpath("/html/body/div/div[2]/form/input[5]")
			submit.click()
			if browser.find_elements_by_css_selector('body > div > div:nth-child(8) > div:nth-child(5)'):
				print("success")
				break

