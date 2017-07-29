# Amount left after min payment over a year

def remainBalance(amt):  
    monthlyPay = 0
    monthlyInterestRate = annualInterestRate/12
    totalPay = 0
        #For each month:
    for x in range(12):
        #Compute the monthly payment, based on the previous month’s balance.
        amt = (amt - amt*monthlyPaymentRate) * (1 + monthlyInterestRate)
    amt = round(amt,2)
    print("Remaining balance: " + str(amt))
        
balance = 484; annualInterestRate = 0.2; monthlyPaymentRate = 0.04

remainBalance(balance)
