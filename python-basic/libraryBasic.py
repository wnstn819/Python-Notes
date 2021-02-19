# sum 함수 - iterable(리스트, 사전 자료형, 튜플형)만 가능
# result = sum([1,2,3,4,5])
# print(result)

# min 함수
# result = min(1,3,5)
# print(result)

# max 함수
# result = max(1,3,5)
# print(result)

# eval 함수 - 숫자 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
# result = eval("(3 + 3) * 7 - 10")
# print(result)

# sorted 함수 - iterable 정렬
# result = sorted([6,4,2,7,2,9]) - 오름차순
# print(result)
# result1 = sorted([6,4,2,7,2,9],reverse = True) - 내림차순
# print(result1)

# sorted 함수 - iterable - key로 정렬
# result = sorted([('홍길동', 35),('이순신', 75),('아무개',50)], key = lambda x: x[1], reverse = True)
# print(result)

# iterable객체는 기본적으로 sort 함수 내장이라 sorted 쓸 필요는 없다
# result = [9,1,8,5,4]
# result.sort()
# print(result)