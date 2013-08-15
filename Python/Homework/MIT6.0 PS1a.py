
#Problem Set 1a
#Name: Mark O'Brien
#Collaborators:  probably Google
#Time Spent:  30min

OriBal=float(input("What is the outstanding balance in 00.00 notation?  "))
AnnInt=float(input("What is the Annual Interest Rate in decimal notation?  "))
MinRat=float(input("What is the min monthly payment rate in decimal notation?  "))

IntPai=(AnnInt/OutBal)*12
MinMPa=OutBal*MinRat
PriPai=MinMPa-IntPai
OutBal=OriBal

for i in range(1,13)
    inc=i+1
    
