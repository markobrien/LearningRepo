#Problem Set:    1b
#Name:           Mark O'Brien
#Collaborators:  Google
#Time Spent:     ?
#Problem B is set to determine the amount needed to pay off the bill w/in a year
#on a monthly basis using a $10 increment.

Balanc=float(input("What is the outstanding balance?  "))
AnnInt=float(input("What is the Annual Interest Rate as decimal?  "))
Payment=0
Chg_Bal=0
month=0
while Chg_Bal>=0 and month<=12:
    for month in range(12):
        Balanc=(AnnInt/12*Balanc)+Balanc
        print(round(Balanc,2))
        Chg_Bal=Balanc-Payment
        print(round(Chg_Bal,2))
        Payment+=10
        month+=1


http://www.snip2code.com/Snippet/2702/MIT-6-00SC--Problem-Set-1b
