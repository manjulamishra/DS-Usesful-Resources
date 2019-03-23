# n is a positive integer.
# Return the nth number in the Fibonacci sequence:
# 0, 1, 1, 2, 3, 5, 8, 13 . . . 
# If n = 5, the function would return 3 because 3 is the 5th number in the Fibonacci sequence.

#Manjula:

def nth_fib_function(n):
  #remove the pass and put in your code
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else: return nth_fib_function(n-1) + nth_fib_function(n-2)
print(nth_fib_function(5))
