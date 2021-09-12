"""
# URL : http://localhost:8080/cgi-bin/pic_web.py
예측버튼 누르면 사진 출력
"""
import sys
import codecs
import cgi
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())
def displayWEB(result=""):
    print('Content-Type:text/html;charset=utf-8\n')
    print("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>sign web By Kang</title>
    </head>
    <body align="center" vertical="middle">
    <form>
        <br><br>
        **이미지 url 입력**<p/>
        url : <input type="text" name="sign" autofocus required placeholder="url을 입력해주세요">
        <input type="submit" value="출력">
        <br><br>
        <img src = {} alt = "이미지 출력 공간" width = "300">
    </form>
    </body>
    </html>
    """.format(result))

form = cgi.FieldStorage()
sign = form.getvalue('sign')

result = sign
result = '{}'.format(result)

displayWEB(result)
