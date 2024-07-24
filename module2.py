import numpy_financial as npf
import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt

#?npf.pv

npf.pv(rate = 0.05, nper = 10, pmt = 0, fv = 10000)
pv = 10000/(1+0.05)**10
print(pv)

-npf.pv(rate = 0.035, nper = 3, pmt = 0, fv = 100)
pv = 100/(1+0.035)**3

##############################

-npf.pv(rate = 0.04, nper = 3, pmt = 3, fv = 100)


##############################


bond_yields = np.arange(0,20,0.1)
print(bond_yields)
bond = pd.DataFrame(bond_yields, columns = ['bond_yields'])
bond['bond_price'] = -npf.pv(rate = bond['bond_yield']/100, nper = 10, pmt = 5, fv = 100)
print(bond)

plt.plot(bond['bond_yield'], bond['bond_price'])
plt.xlabel('Yield (%)')
plt.ylabel('Bond Price (USD)')
plt.title("10 Year Bond 5% Annual Coupon")
plt.show()


##############################

ytm = (100/90.19)**(1/3) - 1
print(ytm)
npf.rate(nper =3, pmt = 3, pv = -97.22, fv = 100)

##

# Calculate the upfront investment at 3% interest
pv_three_percent = -npf.pv(rate = 0.03/12, nper = 7*12, pmt = -100, fv = 11000)

# Print the result
print("3% Annual Interest: ", pv_three_percent)


# Calculate the upfront investment at 4% interest
pv_four_percent = -npf.pv(rate = 0.04/12, nper = 7*12, pmt = -100, fv = 11000)


# Print the result
print("4% Annual Interest: ", pv_four_percent)


# Calculate the upfront investment at 5% interest
pv_five_percent = -npf.pv(rate = 0.05/12, nper = 7*12, pmt = -100, fv = 11000)

# Print the result
print("5% Annual Interest: ", pv_five_percent)

##

# Calculate price of a 3 year 5% yield zero coupon bond

price_1 = 100/(1+0.05)**3

# Print the result
print("3 year 5% yield ZCB: ",price_1 )

# Calculate price of a 10 year 5% yield zero coupon bond
price_2 = 100/(1+0.05)**10

# Print the result
print("10 year 5% yield ZCB: ", price_2)

# Calculate price of a 10 year 5% yield zero coupon bond
price_3 = 100/(1+0.07)**3

# Print the result
print("3 year 7% yield ZCB: ", price_3)

# Find the price of a 10 year bond with 3% coupon and 4% yield
bond_yield_4 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)

# Print the result
print("4% Yield Price: ", bond_yield_4)

# Find the price of a 10 year bond with 3% coupon and 3% yield
bond_yield_3 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)


# Print the result
print("3% Yield Price: ", bond_yield_3)

# Find the price of a 10 year bond with 3% coupon and 5% yield
bond_yield_5 = -npf.pv(rate=0.05, nper=10, pmt=3, fv=100)

# Print the result
print("5% Yield Price: ", bond_yield_5)

# Find the price of a 10 year bond with 2% coupon and 4% yield
bond_coupon_2 = -npf.pv(rate=0.04, nper=10, pmt=2, fv=100)

# Print the result
print("2% Coupon Price: ", bond_coupon_2)

# Find the price of a 10 year bond with 5% coupon and 4% yield
bond_coupon_5 = -npf.pv(rate=0.04, nper=10, pmt=5, fv=100)


# Print the result
print("5% Coupon Price: ", bond_coupon_5)

# Create an array of bond yields and convert to DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add columns for different bonds
bond['bond_price_5Y'] = -npf.pv(rate = bond['bond_yield']/100, nper = 5, pmt = 5, fv = 100)
bond['bond_price_10Y'] = -npf.pv(rate = bond['bond_yield']/100, nper = 10, pmt = 5, fv = 100)

# Plot graph of bonds
plt.plot(bond['bond_yield'], bond['bond_price_5Y'], label='5 Year Bond')
plt.plot(bond['bond_yield'], bond['bond_price_10Y'], label='10 Year Bond')
plt.xlabel('Yield (%)')
plt.ylabel('Bond Price (USD)')
plt.legend()
plt.show()

# Find the first zero coupon bond yield
bond_1 = (100/84.67)**(1/5) - 1

# Print the result
print("ZCB Price USD 84.67: ", bond_1)

# Find the second zero coupon bond yield
bond_2 = (100/78.22)**(1/5) - 1

# Print the result
print("ZCB Price USD 78.22: ", bond_2)

# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = npf.rate(nper=3, pmt=3, pv=-92, fv=100)
print("Bond A: ", bond_a)

# Bond with price of USD 102 paying 6% coupon for 5 years
bond_b = npf.rate(nper=5, pmt=6, pv=-102, fv=100)
print("Bond B: ", bond_b)

# Bond with price of USD 95 paying 3% coupon for 5 years
bond_c = npf.rate(nper=5, pmt=3, pv=-95, fv=100)
print("Bond C: ", bond_c)