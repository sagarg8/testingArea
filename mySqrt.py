counter = 0

def mySqrt(x):
  y = (x+1)/2

  count = counter

  if abs((round(y**2, 3)) - x) > 0.001:
    z = (y + x/y)/2
    mySqrt(z)
    while abs((round(y**2, 3)) - x) > 0.001:
      count = count+1
      #return(print(count))

  else:
    y = round(y, 3)
    return(print(y, count))

mySqrt(9)