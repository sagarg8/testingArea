temp = input("enter temp")
degree = int(temp[:1])
X = temp[-1]

if X.upper() == "C":
   fara = degree*1.8+32
   print(fara."farenheit")
   
elif X.upper() == "f":
   cels = (degree-32)*5/9
   print(cels."Celsius")
