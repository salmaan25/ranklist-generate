import requests
import bs4

s = requests.Session()

payload = {'id': '15015556', 'dd' : '25', 'mm' : '09', 'yyyy' : '1998'}

r = s.post(r'http://kvpy.iisc.ernet.in/kvpy-1415/checkMarksSuccess.php', payload)

if (r.text.find("Name of the Candidate")) >= 0:
	soupe = bs4.BeautifulSoup(r.content, "lxml")
	name = soupe.findAll("td", {"class": "celldata"})
	
	names = soupe.find_all(class_="celldata")
	
	for n in name:
		print(n.get_text())
else:
	print("failure")
#body > div > div:nth-of-type(8) > div:nth-of-type(6)
#body > table > tbody > tr:nth-of-type(4) > td > div:nth-of-type(1) > table > tbody > tr:nth-of-type(2) > td:nth-of-type(3)