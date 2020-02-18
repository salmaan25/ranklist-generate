import csv

def Applicatio_No(path):
	rank_list = open(path, 'r')
	lines = csv.reader(rank_list)
	List_appn_no = []
	for line in lines:
		#print(line)
		if line[0].isdigit():
			a = (line[0], line[1])
			List_appn_no.append(a)
	return List_appn_no
