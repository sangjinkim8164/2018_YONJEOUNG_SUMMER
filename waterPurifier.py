# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 22:47:52 2018
@author: KSJ
"""

## 변수 선언
raw_w = "water"

## 함수 정의
# 1. 정수하는 기능
def clearWater(w) :  
    cle_w = "cleared " + w
    return cle_w

# 2. 온수 만들기
def heatingWater(w) :
    heat_w = "hot " + clearWater(w)
    return heat_w
    
# 3. 냉수 만들기
def coolingWater(w) :
    col_w = "cold " + clearWater(w)
    return col_w

# 4. 얼음물
def addIce(w) :
    ice_w = clearWater(w) + " added ice"
    return ice_w

## 반복문 실행
while True :

    # 사용자 요청 받기
    userInput = input("'온수, 냉수, 얼음물, 전원끄기' 중에 하나를 입력하세요: ")
    
    # 요청에 따른 기능 동작
    
    # 1. 온수를 선택했을 때
    if userInput == "온수" :
        a = heatingWater(raw_w)
        print(a + "가 나왔습니다")
    
    # 2. 냉수를 선택했을 때
    elif userInput == "냉수" :
        a = coolingWater(a)
        print(a + " 가 나왔습니다")
        
    # 3. 얼음물을 선택했을 때
    elif userInput == "얼음물" :
        a = addIce(a)
        print(a + "가 나왔습니다")
    
    elif userInput == "전원끄기" :
        print("작동을 중지합니다")
        break
    
    # 4. 다른 값을 입력했을 때
    else :
        print("잘못된 요청입니다")