반복되는 데이터 처리 라이브러리

permutations - iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수 계산
클래스 이므로 객체 초기화 이후 리스트 자료형으로 변환하여 사용
from itertools import permutations

data = ['A','B','C']
result = list(permutations(data,3)) #모든 순열 구하기

print(result)


product - permutations 와 같이 r개의 데이터를 봅아 일렬로 나열하는 모든 경우의 수 계산 - 중복이 가능함 ex) a,a,a   b,b,b
클래스 이므로 객체 초기화 이후 리스트 자료형으로 변환하여 사용
from itertools import product

data = ['A','B','C']
result = list(product(data,repeat=3))

print(result)



combinations - iterable 객체에서 r개의 데이터를 뽑아 순서를 고려ㅏ지 않고 나열하는 모든 경우를 제시 - 같은 a,b,c가 a,c,b 이렇게 중복 안되게
클래스 이므로 객체 초기화 이후 리스트 자료형으로 변환하여 사용
from itertools import combinations

data = ['A','B','C']
result = list(combinations(data,3))

print(result)



combinations_with_replacement -  combinations와 같이 리스트와 같은 iterable 객체서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산 - 원소를 중복해서 뽑음
from itertools import combinations_with_replacement

data = ['A','B','C']
result = list(combinations_with_replacement(data,3))

print(result)
