while 문
i = 1
result = 0
while i <= 9:
  if i%2==1:
   result += i
  i = i+1
print(result) 



for 문
result = 0
for i in range(1,10):
  result += i
print(result)


for 문 배열 찾기
scores = [90,85,77,65,97]

for i in range(5):
  if scores[i] >= 80:
    print(i+1 , "번 학생은 합격입니다.")



for 문 배열에서 조건
scores = [90,85,77,65,97]
cheatting_list = {2,4}

for i in range(5):
  if i + 1 in cheatting_list:
    continue
  if scores[i] >= 80:
    print(i+1, "번 학생은 합격입니다.")


구구단 만들기
for i in range(1,10):
  for j in range(1,10):
    print(i, "x", j, "=", i*j)
    
  print() 
