"""
# URL : http://localhost:8080/cgi-bin/friend1.py
전송버튼 누르면 friend.py로 입력정보 전송
"""
import sys
import codecs
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-Type:text/html;charset=utf-8\n')
print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body align="center" vertical="middle">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br>
**정보 입력**<p/>
<form action="friend.py" method="POST">
이름 : <input type="text" name="name">&nbsp&nbsp<br>
전화 : <input type="text" name="phone">&nbsp&nbsp</br>
성별 :
<input type="radio" name="gender" value="남" checked="checked">남자
<input type="radio" name="gender" value="여">여자
<br><br>
<input type="submit" value="전송">
</form>
</body>
</html>
""")
