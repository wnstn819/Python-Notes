import time
start_time = time.time()


array = [3,5,1,2,4]
sumary = 0

for x in array:
  sumary += x

print(sumary)



end_time = time.time()
print("time: ", end_time - start_time)
