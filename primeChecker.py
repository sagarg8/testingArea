def isPrime(num):
  """ The function returns True if num is prime and False otherwise"""
  if num<2:
    return(print(False))  
  for i in range(2, num):
    if num%i == 0:
      return(print(False))
  else: return(print(True))

isPrime(3)