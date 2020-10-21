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

a = "https://global.sitesafety.trendmicro.com/result.php"
b = "https://registry.npmjs.org/@trendmicro/react-portal/-/react-portal-1.0.1.tgz"
