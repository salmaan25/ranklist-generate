from find_details import find_details
from Applicatio_No import Applicatio_No
from docx import Document

document = Document()
table = document.add_table(rows = 1, cols = 9)
table.style = 'TableGrid'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Rank'
hdr_cells[1].text = 'Appn. No'
hdr_cells[2].text = 'Name'
hdr_cells[3].text = 'Seat No.'
hdr_cells[4].text = 'Stream'
hdr_cells[5].text = 'Aptitude Marks'
hdr_cells[6].text = 'Interview Marks'
hdr_cells[7].text = 'Total'
hdr_cells[8].text = 'DOB'
cur_row = 1
List_appn_no = Applicatio_No(r'2017-SA-GEN-trial.csv')
#print(List_appn_no)
for application in List_appn_no:
	row = table.add_row()
	table.style = 'TableGrid'
	hdr_cells = table.rows[cur_row].cells
	
	details_DOB = find_details(application[1])
	details = details_DOB[0]
	DOB = details_DOB[1]

	hdr_cells[0].text = application[0]
	hdr_cells[1].text = details[0].get_text()[3:]
	hdr_cells[2].text = details[1].get_text()[3:]
	hdr_cells[3].text = details[2].get_text()[3:]
	hdr_cells[4].text = details[3].get_text()[3:]
	hdr_cells[5].text = details[5].get_text()[3:]
	hdr_cells[6].text = details[6].get_text()[3:]
	hdr_cells[7].text = details[7].get_text()[3:]
	hdr_cells[8].text = DOB
	cur_row += 1
document.save('Rank_list.docx')

#2017-SA-GEN-trial.csv
#tabula-2017-SA-GEN.csv