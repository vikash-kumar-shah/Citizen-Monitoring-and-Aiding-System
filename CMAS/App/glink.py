import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
def collect(user_error):
	s=""
	
	
	scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.								from_json_keyfile_name("JFILE.json", scope)
	client = gspread.authorize(creds)
	sheet = client.open("Now").sheet1
	LIST=sheet.get_all_records()
	c=sheet.row_values(5)
	for DICT in LIST:
		if DICT["Person"]==user_error:
			s=DICT["Date"]+"  :"+DICT["Time"]+"  :"+DICT["Person"]+"\n"+s
	"""for value in c:
		
		s=s+value+"-"  """
	print(s)
	print("success")
	return s
collect("Person1")




