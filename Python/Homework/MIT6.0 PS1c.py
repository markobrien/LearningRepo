#Problem Set:    1c
#Name:           Mark O'Brien
#Collaborators:  none
#Time Spent:     x hrs
#A follow on to PS1B, but use bisection to more quickly get montly payment
#and more accurately, within a few cents instead of $10 increments.

balanc = float(input("What is the outstanding balance?  "))
annual_int = float(input("What is the Annual Interest Rate as decimal?  "))
chg_bal = (balanc * (1 + annual_int))       #balance + the interest accumulated
lower_boundary = chg_bal / 12               #for the bisection
upper_boundary = (chg_bal ** 12) / 12
payment = 0
epsilon = .01                               #is the answer this close?
bisect_shift = (lower_boundary + upper_boundary)/2.0
while (chg_bal - (12 * payment)) >= epsilon and bisect_shift != chg_bal:
    payment += .01        
    if (bisect_shift) < chg_bal:
        lower_boudary = bisect_shift
    else:
        upper_boundary = bisect_shift
print ("RESULT")
print ("Monthly payment needed to pay off in one year", round(payment,2))

    
    
