from jira import JIRA
import datetime
from datetime import date

username = 'TestingUser2'
password = 'PassPass'
coc_jira = JIRA('http://another-sample-url.trendmicro.com',auth=(username, password))

dt = datetime.datetime.today()
currentMonth = date(day=dt.day, month=dt.month, year=dt.year).strftime('%B %Y')
#print(currentMonth)# upload file from `/some/path/attachment.txt`
#coc_jira.add_attachment(issue=issue_key, attachment='requirements.txt')
