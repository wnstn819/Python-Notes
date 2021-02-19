코딩테스트에서 자주 사용되는 deque와 Counter를 제공
deque를 이용해서 queue를 구현
리스트는 삽입(append), 삭제(pop)와 같은 다양한 기능이 있지만 추가와 삭제를 할때 가장 뒤쪽 원소를 기준으로 수행된다. 앞쪽의 원소를 처리할 때에는 복잡도가 O(N)으로 높기 때문에 queue를 사용한다.
인덱싱, 슬라이싱 x, 연속적으로 나열된 데이터의 시작이나 끝부분에 데이터를 넣을 경우 효율적 스택 , 큐의 기능 모두 포함
appendleft() - 첫번째 원소 삽입, append() - 마지막 원소 삽입
popleft() - 첫번째 원소 삭제, pop - 마지막 원소 삭제

왼쪽 오른쪽 값 추가
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)
data.append(6)
data.appendleft(0)
print(data)
print(list(data))


원소별 등장횟수 셀 때
from collections import Counter
 
counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['red'])
print(dict(counter))

