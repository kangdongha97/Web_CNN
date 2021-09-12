"""
# URL : http://localhost:8080/cgi-bin/sign_web.py
예측버튼 누르면 사진 출력
"""
import sys
import codecs
import cgi
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())
def displayWEB(result = "",result2 = "", result3 = ""):
    print('Content-Type:text/html;charset=utf-8\n')
    print("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>sign web By Kang</title>
    </head>
    <body align="center" vertical="middle" height:200%;>
    <form>
        <br><br>
        **이미지 url 입력**<p/>
        url : <input type="text" name="sign" autofocus required placeholder="url을 입력해주세요">
        <input type="submit" value="판정">
        <br><br>
        <div style='text-align:center; background-color:#D5D5D5;border-radius:10px; width:80%; height:450px; margin: auto; padding:25px;'>
            <br>
            <img src = {} alt = "이미지 출력 공간" width = "300" height = "300" style="margin-top:10px; margin-bottom:10px; margin-right:10%;">
            <img src = {} alt = "" width = "300">
            
            <p><font color = 'black' font size = '5'><br> 입력사진 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 예측결과 </font></p>
        </div>
        
        
        <p><font color='blue' font size = '5'>{}</font></p>
    </form>
    </body>
    </html>
    """.format(result, result2, result3))


#(1) 모델 로딩
from keras.models import load_model
from keras.preprocessing import image
import cv2
import numpy as np
import os

model_file = 'C:/Users/KangDongha/Python/web/cgi-bin/model_trained_data.h5'
model = load_model(model_file)

#(2) web 페이지 Input 리스트 가져오기 url 사진 출력
form = cgi.FieldStorage()
sign = form.getvalue('sign')

result = sign
result = '{}'.format(result)

#(3) 가져온 사진 전처리
#사진 저장


import urllib.request
url = sign

#판정하기
def predict_class(Pred):
    if(classIndex == 0):
        return 'No Left Turn'
    elif(classIndex == 1):
        return 'Speed Bump'
    elif(classIndex == 2):
        return 'U Turn'
        
if url is not None:
    savename = 'Input.PNG'
    urllib.request.urlretrieve(url, "C:/Users/KangDongha/Python/web/cgi-bin" + "/" + savename)


    #이퀄라이징, 해상도 변경
    U_img = "C:/Users/KangDongha/Python/web/cgi-bin"
    U_img_path = os.path.join(U_img, 'Input.PNG')
    U_img_load = image.load_img(U_img_path)

    U_img_np = image.img_to_array(U_img_load)

    U_img_Equ = cv2.imread(U_img_path, 0)
    U_img_Equ = cv2.equalizeHist(U_img_Equ)

    U_img_Equ = cv2.resize(U_img_Equ, (32, 32))
    cv2.imwrite('C:/Users/KangDongha/Python/web/cgi-bin/Input2.PNG', U_img_Equ)
    U_img_Equ = U_img_Equ.reshape(1, 32, 32, 1)

    classIndex = model.predict_classes(U_img_Equ)
    result3 = predict_class(classIndex)
    
    if(classIndex == 0):
        result2 = 'http://gdimg.gmarket.co.kr/1209519029/still/600?ver=1514565573'
    elif(classIndex == 1):
        result2 = 'http://image.auction.co.kr/itemimage/b1/04/a4/b104a4666.jpg'
    elif(classIndex == 2):
        result2 = 'http://gdimg.gmarket.co.kr/1207358763/still/600?ver=1514451353'
        
    result2 = '{}'.format(result2)
    
    result3 = '{} 입니다.'.format(result3)
    
else :
    result2 = ''
    result3 = '이미지가 없습니다. url을 입력해주세요.'
    

displayWEB(result, result2, result3)
