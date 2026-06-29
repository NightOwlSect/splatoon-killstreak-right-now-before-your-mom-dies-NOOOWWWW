def fibonacci_loop(n):
  # assume n is a non-negative integer
  f_i = list(range(n+1))
  for i in range(2, n+1):
    f_i[i] = f_i[i-1] + f_i[i-2]
  return f_i[n]

n = int(input("Which Fibonacci number do you want to calculate?"))
print(fibonacci_loop(n))
