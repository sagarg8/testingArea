def personalAllowance(salary): #works out untaxable remainder of salary 

  if salary>100001:
    remainder = salary-100000
    allowance = 12500 - remainder/2
    if allowance<0:
       allowance = 0

  else:
    allowance = 12500   

  return(allowance)


def incomeTax(income):  #works out the tax on a given yearly salary
  taxable = income - personalAllowance(income)

  if personalAllowance(income)>income:
    taxed = 0

  elif taxable<=37500: #if income is less than 37.5k
    taxed = taxable*0.2

  elif taxable<150000: #if 37.5k<income<150k
    taxable1 = taxable - 37500
    taxed = taxable1*0.4 + 37500*0.2

  else: #if income greater than 150k
    taxable1 = taxable - 150000
    taxed = taxable1*0.45 + 112500*0.4 + 37500*0.2
    
  return(taxed)


def nationalInsurance(wage): #works out NI tax on a weeks salary
  if wage<183:
    final = 0
  elif wage<962:
    final = (wage-183)*0.12
  else:
    wage1 = wage-961
    final = wage1*0.02 + ((961-183)*0.12)

  return(final)

incomeTax(30000)

def monthlyPay(income):   #input should be a months wage
  weekly = income/4.33    #makes input for the NI function easier by making it a weekly income
  niTax = nationalInsurance(weekly)*4.33  #turns the weekly NI tax into a monthly tax
  
  yearly = income*12            #works out a years salary for the function
  inTax = incomeTax(yearly)/12  #works out 1 months income tax

  fullyTaxed = (niTax + inTax)
  taxFree = income - fullyTaxed

  return(print(fullyTaxed, taxFree))


def monthlyPayExt(income, loan):   #input should be a months wage, and a bool value to check whether the user has a student loan
  weekly = income/4.33    #makes input for the NI function easier by making it a weekly income
  niTax = nationalInsurance(weekly)*4.33  #turns the weekly NI tax into a monthly tax
  
  yearly = income*12            #works out a years salary for the function
  inTax = incomeTax(yearly)/12  #works out 1 months income tax

  slcTax = 0.09*income        #works out a months SLC tax on income
  
  if loan == True and yearly>25725:   #if they earn enough and have a loan, they will be charged the 3rd tax
    fullyTaxed = (niTax + inTax + slcTax)

  else:       #else in any other case, just the 2 taxes
    fullyTaxed = (niTax + inTax)

  taxFree = income - fullyTaxed

  return(print(fullyTaxed, taxFree))

monthlyPayExt(2000, False)