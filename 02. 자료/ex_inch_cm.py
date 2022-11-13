# inch 단위의 자료를 입력받아 cm 단위를 구하는 예제(1inch = 2.54cm)

str_input = input("숫자 입력> ")
num_input = int(str_input)

print()
print(num_input, "inch")
print((num_input * 2.54), "cm")