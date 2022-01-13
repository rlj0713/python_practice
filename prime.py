import time

start_time = time.perf_counter()

list_of_primes = [2]
old_list = [2]

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

j = 1
while len(list_of_primes) <= 10001:
  for k in old_list:
    if j % k != 0:
      if is_prime(j):  
        list_of_primes.append(j)
        old_list.insert(0, j)
      j += 1

print(list_of_primes[-2])


end_time = time.perf_counter()
print(f"Execution Time : {end_time - start_time:0.6f}" )

