# 입력 받기
string = input("입력> ")

# 출력
print("입력 + 100", string+100)

# TypeError: can only concatenate str (not "int") to str : "입력한 값"+100이 되어 문자열과 숫자는 더할 수 없음. 
#                                                          "입력한 값"을 숫자로 변환해야 숫자 연산에 활용할 수 있다는 뜻