import time

start_time = time.perf_counter()

list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]

def is_prime(x):
  
  y = x / 2

  count = 0
  for i in range(1, int(y), 2):
    if x % i == 0:
      count += 1
      if (count > 1):
        return False
  if count <= 1:
    return True

j = 2
while len(list_of_primes) <= 10001:
  if j % 2 != 0 and j % 3 != 0 and j % 5 != 0 and j % 7 != 0 and j % 11 != 0 and j % 13 != 0 and j % 17 != 0 and j % 19 != 0 and j % 23 != 0 and j % 29 != 0 and j % 31 != 0 and j % 37 != 0 and j % 41 != 0 and j % 43 != 0 and j % 47 != 0 and j % 53 != 0 and j % 59 != 0 and j % 61 != 0 and j % 67 != 0 and j % 71 != 0 and j % 73 != 0 and is_prime(j):  
    list_of_primes.append(j)
  j += 1

print(list_of_primes[-2])


end_time = time.perf_counter()
print(f"Execution Time : {end_time - start_time:0.6f}" )

