sal=0
name=input("Enter Employee Name : ")
mon=int(input("Enter Month By its number(1-12): "))
days=int(input("Enter Number of Working Days(1-31): "))

if mon in {1,3,5,7,8,10,12} and days<=31:
  des=input("Enter Designation(M,TL,TM) :")
  ot=int(input("Enter Overtime Days : "))
  if des=='M':
    if ot==0:
      sal=2000*days
    else:
      sal=(2000*days)+((2000/2)*ot)
    print("Salary : ",sal)
  elif des=='TL':
    if ot==0:
      sal=2000*days
    else:
      sal=(2000*days)+((2000/2)*ot)
    print("Salary : ",sal)
  elif des=='TM':
    if ot==0:
      sal=1500*days
    else:
      sal=(1500*days)+((1500/2)*ot)
    print("Salary : ",sal)
  else:
    print("Invalid Choice.")
elif mon in{4,6,9,11} and days<=30:
  des=input("Enter Designation(M,TL,TM) :")
  ot=int(input("Enter Overtime Days : "))
  if des=='M':
    if ot==0:
      sal=2000*days
    else:
      sal=(2000*days)+((2000/2)*ot)
    print("Salary : ",sal)
  elif des=='TL':
    if ot==0:
      sal=2000*days
    else:
      sal=(2000*days)+((2000/2)*ot)
    print("Salary : ",sal)
  elif des=='TM':
    if ot==0:
      sal=1500*days
    else:
      sal=(1500*days)+((1500/2)*ot)
    print("Salary : ",sal)
  else:
    print("Invalid Choice.")
elif mon in {2} and days<=29:
  des=input("Enter Designation(M,TL,TM) :")
  ot=int(input("Enter Overtime Days : "))
  if des=='M':
    if ot==0:
      sal=2000*days
    else:
      sal=(2000*days)+((2000/2)*ot)
    print("Salary : ",sal)
  elif des=='TL':
    if ot==0:
      sal=2000*days
    else:
      sal=(2000*days)+((2000/2)*ot)
    print("Salary : ",sal)
  elif des=='TM':
    if ot==0:
      sal=1500*days
    else:
      sal=(1500*days)+((1500/2)*ot)
    print("Salary : ",sal)
  else:
    print("Invalid Choice.")
else:
  print("Invalid Choices.")
  
  
  
  
#Output
  
#Enter Employee Name : PV
#Enter Month By its number(1-12): 3
#Enter Number of Working Days(1-31): 31
#Enter Designation(M,TL,TM) :M
#Enter Overtime Days : 0
#Salary :  62000
  
  
