# 다익스트라 최단 경로 알고리즘, 우선순위 큐 기능 구현
# 최소 힙으로 구성 원소를 전부 힙에 넣었다 빼는 것만으로 O(NlogN)에 오름차순 정렬이 완료된다.
# 최소 힙 자료구조의 최상단 원소는 '가장 작은' 원소
# 삽입 heapq.heappush(), 원소 꺼낼 때 heapq.heappop()

# 힙 정렬하는 예제
# import heapq

# def heapsort(iterable):
#   h = []
#   result = []
#   # 모든 원소 차례대로 힙에 삽입
#   for value in iterable:
#     heapq.heappush(h, value)
#   # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#   for i in range(len(h)):
#     result.append(heapq.heappop(h))
#   return result

# result = heapsort([1,3,5,7,9,2,4,6,8,10])
# print(result)

# heapq에서는 최대 힙을 제공 하지 않기때문에 원소의 붛를 임시로 변경하는 방식을 사용한다. 부호를 잠시 반대로 바꿨다가(음수로 바꿔서) 원소를 꺼낸 뒤에 다시 부호를 바꾸면 된다.

# import heapq

# def heapsort(iterable):
#   h = []
#   result = []
#   # 모든 원소를 차례대로 힙에 삽입
#   for value in iterable:
#     heapq.heappush(h,-value)
   
#   # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#   for i in range(len(h)):
#     result.append(-heapq.heappop(h))
#   return result

# result = heapsort([1,3,5,7,9,2,4,6,8,10])
# print(result)