import numpy_financial as npf
import matplotlib.pyplot as plt

"""

Net Present value (NPV)
NPV : financiële maatstaf die de totale waarde van een investeringsmogelijkheid probeert weer te geven. 
NPV = cash flows / (1 + interestrate) ^time of the cash flow


Ik ga gedurende 3 jaar investeren in een project waar ik initieel 
€100 000 heb betaald. Ik krijg ervan €50 000 per jaar terug. De interestrate is 5%. 

"""

# 1. variabelen declareren
time = 4
CF0 = -100000 
CF1 = 50000
CF2 = 50000
CF3 = 50000
interestrate = 0.05

# 2. Lijst maken met de cashflows
Cashflows = [CF0,CF1,CF2,CF3]

"""

Manier 1

* Functie NPV maken 
def NPV(interestrate,Cashflows):
    NPV = 0
    for i in range(len(Cashflows)):
        NPV = NPV + Cashflows[i] / (1 + interestrate)** i
    return NPV
print(NPV(0.05,Cashflows))

"""

# Manier 2

npv = npf.npv(interestrate, Cashflows)
print("De net present value is €%3.4f"%npv)

"""

Internal rate of return (IRR)
IRR : de discont rate die de NPV-formule oplost wanneer de NPV gelijk is aan nul.

"""

# IRR berekenen
irr = round(npf.irr(Cashflows),4)
print("de internal rate of return is %3.4f"%irr)

"""

Future Value (FV)
FV : de waarde van een aanwinst naar een toekomstige datum, rekening houdend met de tijdswaarde van geld.

"""

fv = npf.fv(interestrate,time, -50000,100000)
print("de future value is €%3.4f"%fv)

# gebruik van Matplotlib
y = [npf.fv(interestrate,i,-50000,100000) for i in range(4)]
print([npf.fv(interestrate,i,-50000,100000) for i in range(4)])
plt.plot(y)
plt.ylabel("Investment Value")
plt.xlabel ("Years " )
plt.show()