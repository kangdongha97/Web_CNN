import sys
import codecs
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())
import cgi
form = cgi.FieldStorage()
name = form['name'].value
phone = form['phone'].value
gender = form['gender'].value

print('Content-Type:text/html;charset=utf-8\n')
print("""
<html>
<body align="center">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br>
이름 :  {}<br><br> 전화번호 :  {}<br><br> 성별 :  {}<br><br>
<input type = "button" value = "뒤로" onclick = "history.back()">
</body>
</html>
""".format(name, phone, gender))
