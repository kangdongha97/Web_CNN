"""
-----anaconda prompt-----
cgi-bin 폴더 바로 위
cd /Users/KangDongha/Python/web

-----로컬 호스트 서버-----
python -m http.server 8080 --cgi
C:/Users/KangDongha/Python/web>python -m http.server 8080 --cgi
주소창에 URL 입력
URL : http://localhost:8080/cgi-bin/iris-web.py

-----외부 접근가능 서버-----
공유기 포트포워드 설정
python -m http.server --bind 192.168.0.10 8080 --cgi
C:/Users/KangDongha/Python/web>python -m http.server 192.168.0.10 8080 --cgi
주소창에 URL 입력
URL : http://192.168.0.10:8080/cgi-bin/iris-web.py
"""
# 모듈 로딩 ---------------------------------------------------
import cgi, sys, codecs, os
from keras.models import load_model
file_name='iris_model.h5'

# WEB 인코딩 설정 ---------------------------------------------
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())
labels = {
    'Iris-setosa': [1, 0, 0],
    'Iris-versicolor': [0, 1, 0],
    'Iris-virginica': [0, 0, 1]
}

# 함수 선언 --------------------------------------------------
# WEB 페이지 출력 --------------------------------------------
def displayWEB(result=""):
    print("Content-Type: text/html; charset=utf-8")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>IRIS 품종 판별</title>
    </head>
    <body align="center">
    <h2>[ 품 종 정 보 ]</h2>
    <form>
        <div style='text-align:center; background-color:#D5D5D5;border-radius:10px;width:80%; margin: auto;padding:30px;'>
            <input id="s_length" type="text" placeholder="꽃받침길이" name="s_length"> &nbsp&nbsp
            <input id="s_width"  type="text" placeholder="꽃받침너비" name="s_width"> &nbsp&nbsp
            <input id="p_length" type="text" placeholder="꽃잎길이"   name="p_length"> &nbsp&nbsp
            <input id="p_width"  type="text" placeholder="꽃잎너비"   name="p_width">
            <input type="submit" value="판정"></br>
            <p><font color='blue'>{}</font></p>
        </div>    
    </form></body></html>""".format(result))

# 판정 --------------------------------------------------------
def detect_iris(s_l, s_w, p_l, p_w):
    x_new=[[float(s_l), float(s_w),float(p_l),float(p_w)]]
    print(x_new)
    y_pred = model.predict(x_new)

    # 판별 ------------------------------------
    print(f"-y=>{type(y_pred)}, {y_pred.tolist()[0]}")
    _y = y_pred.tolist()[0]
    _y = [round(v) for v in _y]
    print(f"-y=>{_y}")

    for key, value in list(labels.items()):
        if value == _y:
            print(f" Bingo ! {key}")
            return str(key)

# 기능 구현 -----------------------------------------------------
# (1) 모델 로딩 --------------------------------------------
model_file = os.path.dirname(__file__) + "/iris_model.h5"
model=load_model(model_file)

# (2) WEB 페이지 <Form> -> <INPUT> 리스트 가져오기
form = cgi.FieldStorage()
s_length_value = form.getvalue('s_length')
s_width_value  = form.getvalue('s_width')
p_length_value = form.getvalue('p_length')
p_width_value  = form.getvalue('p_width')

# (3) 판정 하기
if s_length_value is not None and s_width_value is not None and p_length_value is not None and p_width_value is not None:
    result = detect_iris(s_length_value, s_width_value, p_length_value, p_width_value)
    result = '해당 품종은 [ {} ] 입니다.'.format(result)
else:
    result ='측정된 결과가 없습니다.'

# (4) WEB 출력하기
displayWEB(result)
