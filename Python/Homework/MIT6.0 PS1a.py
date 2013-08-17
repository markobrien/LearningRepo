#Problem Set 1a
#Name: Mark O'Brien
#Collaborators:  probably Google
#Time Spent:  4hr

Balanc=float(input("What is the outstanding balance?  "))
AnnInt=float(input("What is the Annual Interest Rate as decimal?  "))
MinRat=float(input("What is the min monthly payment rate as decimal?  "))
TotPai=float(0.0)                                         #Total of interest and principle, init outside of loop
for month in range(12):
    IntPai=round((AnnInt/12)*Balanc,2)                  #Calc Interest
    MinMPa=round(Balanc*MinRat,2)                       #Minimum payment due      
    PriPai=round(MinMPa-IntPai,2)                       #Principle Paid
    Balanc=round(Balanc-PriPai,2)                       #Balance after principle paid
    month=month+1
    print ("Month: ", round(month,2))
    print ("Minimm monthly payment: ",round(MinMPa,2))
    print ("Principle paid: ",round(PriPai,2))
    print ("Remaining balance: ",round(Balanc,2))
    TotPai=TotPai+round(PriPai+IntPai,2)
print("Total Paid "),round(TotPai,2)                    #This is not returning a value!!
print("Remaining Balance",round(Balanc,2))
