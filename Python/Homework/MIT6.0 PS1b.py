#Problem Set:    1b
#Name:           Mark O'Brien
#Collaborators:  https://github.com/morganwilde/MIT-opencourceware---6.00/blob/master/2-core-elements-of-a-program/problem-set-1.py
#Time Spent:     5 hrs
#Problem B is set to determine the amount needed to pay off the bill w/in a year
#on a monthly basis using a $10 increment.

balanc = float(input("What is the outstanding balance?  "))
annual_int = float(input("What is the Annual Interest Rate as decimal?  "))
chg_bal = balanc
monthly_int = annual_int / 12
monthly_bal=0
payment = 0
while chg_bal > 0:
    for month in range(13):
        if chg_bal > 0:
            chg_bal = ((1 + monthly_int) * chg_bal) - payment
            if chg_bal <= 0:
                break
    if chg_bal > 0:
        payment += 10
        chg_bal = balanc
    else:
        print ("RESULT")
        print ("Monthly payment needed", payment)
        print ("Number of months needed", month)
        print (round(chg_bal,2))
    
    
