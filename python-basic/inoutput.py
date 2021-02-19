# # 데이터의 개수 입력
# n = int(input())
# # 각 데이터를 공백으로 구분하여 입력
# data = list(map(int, input().split()))

# data.sort(reverse = True)
# print(data)

# n , m, k를 공백으로 구분하여 입력
# n, m ,k = map(int, input().split())

# print(n,m,k)

# input() 은 느려서 sys 라이브러리를 이용해서 더 빠르게 입력할 수 있다. - 시간 초과 방지
# rstrip()은 sys가 전체 입력받고 난 후 엔터를 같이 출력하는데 그 엔터를 없애 주는 명령어이다.
# 입력받은 문자열 전체출력
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

# 입력받은 문자열 띄어쓰기 자르고 0번째 출력 ex = hello world -> hello
# import sys
# data = sys.stdin.readline().rstrip()
# print(data.split()[0])

# 문자열과 숫자를 같이 출력하는 방법
# answer = 7

# print("정답은", answer , "입니다.")
# print("정답은 " + str(answer) + " 입니다.")

# f-string 사용법
# answer = 7
# print(f"정답은 {answer}입니다")

