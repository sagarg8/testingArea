# This is my imperial to metric calc/metric to imperial calc

def metricToImperial(x):      # x is in kilos
    s = 6.35                  # one stone = 6.35kg
    st = 2.2                  # one kg = 2.2lb
    if x%s != 0:
       
        y = int(x/s)          # y finds how many whole stones fit into the given amount of kilos
        z = (x%s)*st          # z finds the remainder of the kilo input and turns it into pounds 
       
        print("You weigh", y, "stones and", z, "pounds!")

        return( ((x%s)*st) + (int(x/s)) )

    else:
        return(x*s)

def imperialToMetric(a, b):    # a is in stones, b is in pounds
    s = 6.35                   # one stone = 6.35kg
    st = 2.2                   # one kg = 2.2lb

    k = a*s     
    kg = b/st
    kilo = k + kg

    print("You weigh", kilo , "Kilograms!")
    return( (a*s) + (b/st) )

metricToImperial(56)
imperialToMetric(8, 5)