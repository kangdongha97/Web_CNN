"""
# URL : http://localhost:8080/cgi-bin/hi.py
"""
import sys
import codecs
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())
print("Content-type: text/html; charset=utf-8")
print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<body align="center">
<h1>안녕하세요 만나서 반가워요</h1>
<h1>This page made by Kang</h1>
<br>
    <img src = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MTJfMTQ2%2FMDAxNjIwODEwMzQ1ODEw.dSVRJedAouG6-yPmHNsQVBJb2R41C9l_01kwop0-h00g.plrHWe0CSt7xTY2VmJwEImPN9fEaMvzaNn1TnQukrYMg.JPEG.skdy119%2F2563F827-0232-48AB-A825-625D472D254A.jpeg&type=sc960_832" alt = "이미지" width = "30%">
<br>
<h1>she is Danbaljwa</h1>
</body>
</head>
</html>
""")