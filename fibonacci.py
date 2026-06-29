def fibonacci_loop(n):
  # assume n is a non-negative integer
  f_i = list(range(n+1))
  for i in range(2, n+1):
    f_i[i] = f_i[i-1] + f_i[i-2]
  return f_i[n]

f_n=[0, 1]

def fibonacci(n):
  gobal f_N
  if len(f_n)n:
    return f_n(n)
  result =fibonacci(n-1)+fibonacci(n-2)
f_n.append(result)
return f_n[n]

n = int(input("Which Fibonacci number do you want to calculate?"))
print(fibonacci_loop(n))
print(fibonacci(n))
