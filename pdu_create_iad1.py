from jira import JIRA
import datetime
from datetime import date

username = 'TestingUsername'
password = 'Password1234'
coc_jira = JIRA('http://exampleurl.trendmicro.com',auth=(username, password))

dt = datetime.datetime.today()
currentMonth = date(day=dt.day, month=dt.month, year=dt.year).strftime('%B %Y')
#print(currentMonth)

# upload file from `/some/path/attachment.txt`
