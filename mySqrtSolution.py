def mySqrt(x):
    y = (x+1)/2
    while not (abs((y**2-x)) < 0.001):
        y = (y + x/y)/2
    return (print(y))

mySqrt(2)   