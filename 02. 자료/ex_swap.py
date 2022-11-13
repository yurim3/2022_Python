# 문자열 두 개를 입력받고 출력하는 프로그램
# Ex. (안녕하세요)(아침입니다) -> 안녕하세요 아침입니다, 아침입니다 안녕하세요

str1 = input("문자열 입력> ")
str2 = input("문자열 입력> ")

print(str1, str2)
a = str1 #a: 안녕하세요
str1 = str2 #str1: 아침입니다
str2 = a #str2: 안녕하세요
print(str1, str2)
