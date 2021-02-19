# 이진 탐색을 쉽게 구현할 수 있도록 제공
# bisect 라이브러리에서는 bisect_left() , bisect_right() -> 시간복잡도 O(logN)
# bisect_left(a, x) - 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) - 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

# from bisect import bisect_left, bisect_right

# a = [10,20,40,40,80]
# x = 4

# print(bisect_left(a,15))
# print(bisect_right(a,15))
# 결과 1 1  ->  a[1], a[1] 에 넣어야됨



# count_by_range 함수
# from bisect import bisect_left, bisect_right

# #값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수 - left_value<= x <= right_value
# def count_by_range(a, left_value, right_value):
#   right_index = bisect_right(a, right_value)
#   left_index = bisect_left(a, left_value)
#   return right_index - left_index

# a = [1,2,3,3,3,3,4,4,8,9]

# #값이 4인 데이터의 개수 출력
# print(count_by_range(a, 4, 4))

# #값이 [-1, 3] 범위에 있는 데이터의 개수 출력
# print(count_by_range(a, -1, 3))


