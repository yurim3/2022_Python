# 원의 반지름을 입력받아 원의 둘레와 넓이 구하는 코드
# 둘레: 2 * 원주율 * 반지름
# 넓이: 원주율 * 반지름 * 반지름

str_input = input("원의 반지름 입력> ")
num_input = float(str_input)
print()
print("반지름: ", num_input)
print("둘레: ", 2 * 3.14 * num_input)
print("넓이: ", 3.14 * num_input * num_input)