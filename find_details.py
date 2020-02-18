import requests
import bs4

def find_details(roll):
	m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
	d = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
	years = ['2001', '2000', '2002']
	with requests.Session() as s:
		for year in years:
			for i in m:
				for j in d:
					payload = {'id': roll, 'dd' : j, 'mm' : i, 'yyyy' : year}
					r = s.post(r'http://kvpy.iisc.ernet.in/kvpy1718/checkMarksSuccess.php', payload)
					soupes = bs4.BeautifulSoup(r.content, 'html.parser')
					marks = soupes.find_all('div', {'class' : 'result_right'})
					dob = j + '-' + i + '-' + year 
					return (marks, dob)


