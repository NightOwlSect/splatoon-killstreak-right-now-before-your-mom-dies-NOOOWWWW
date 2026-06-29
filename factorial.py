# This wont work!
def factorial(n):
  print("Calculating", n, "factorial")
  result = factorial(n-1) * n
  return result

value = factorial(4)
print("4 factorial is", value)
