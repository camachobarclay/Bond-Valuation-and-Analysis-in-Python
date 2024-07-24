import numpy_financial as npf
import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt

-npf.pv(rate = 0.05, nper = 5, pmt = 5, fv = 100)
-npf.pv(rate = 0.05, nper = 10, pmt = 5, fv = 100)

-npf.pv(rate = 0.06, nper = 5, pmt = 5, fv = 100)
-npf.pv(rate = 0.06, nper = 10, pmt = 5, fv = 100)

price = -npf.pv(rate = 0.05, nper = 10, pmt = 5, fv = 100)
price_up = -npf.pv(rate = 0.06, nper = 10, pmt = 5, fv = 100)
price_down = -npf.pb(rate  = 0.04, nper = 10, pmt = 5, fv = 100)
duration = (price_down -price_up)/(2*price*0.01)
print(duration)

####################


bond_maturity = np.arange(0,30,0.1)
bond = pd.DataFrame(bond_maturity,columns = ['bond_maturity'])

bond['price'] = -npf.pv(rate = 0.05, nper = bond['bond_maturity'], pmt = 5, fv = 100)
bond['price_up'] = -npf.pv(rate = 0.05+.01, nper = bond['bond_maturity'], pmt = 5, fv = 100)
bond['price_down'] = -npf.pv(rate = 0.05-.01, nper = bond['bond_maturity'], pmt = 5, fv = 100)
bond['duration'] = (bond['price_down'] - bond['price_up'])/(2*bond['price']*0.01)

plt.plot(bond['bond_maturity'],bond['duration'])
plt.xlabel('Maturity (Years)')
plt.ylabel('Duration (%)')
plt.title("Effect of Varying Maturity On Bond Duration")


###################

# bond with a price of USD 92.28 and duration of 7.98% has dollar duration of
dollar_duration = 92.28*7.98*0.01
print("Dollar Duration: ", dollar_duration)

DV01 = 92.28*7.98*0.0001
print("DV01: ", DV01)

portfolio_dv01 = 10000
bond_dv01 = 0.0736

hedge_quantity = portfolio_dv01/bond_dv01
print("Number of bonds to sell: ", hedge_quantity)

bond_price = 92.28
hedge_amount = hedge_quantity*bond_price
print("Dollar amount to sell: USD", hedge_amount)

# 10 year bond with 4% coupon and 5% yield price USD 92.28 dollar 
# duration of 7.36 estimated bond price change if interest rates drop 3%:
-100*7.36*-0.03

# Actual change from repricing the bond:
-npf.pv(rate = 0.02, nper = 10, pmt = 4, fv = 100) - 92.28


################


##

# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)

# Price a 10 year bond with 3% annual coupon at 4% yield and print
bond_2 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
print("10 Year Bond 4% Yield: ", bond_2)

# Price a 20 year bond with 3% annual coupon at 3% yield and print
bond_3 = -npf.pv(rate=0.03, nper=20, pmt=3, fv=100)
print("20 Year Bond 3% Yield: ", bond_3)

# Price a 20 year bond with 3% annual coupon at 4% yield and print
bond_4 = -npf.pv(rate=0.04, nper=20, pmt=3, fv=100)
print("20 Year Bond 4% Yield: ", bond_4)

price = -npf.pv(rate = 0.03, nper = 10, pmt = 0, fv = 100)
price_up = -npf.pv(rate = 0.04, nper = 10, pmt = 0, fv = 100)
price_down = -npf.pv(rate  = 0.02, nper = 10, pmt = 0, fv = 100)

# Calculate duration using the formula and print result
duration = (price_down -price_up)/(2*price*0.01)
print("Zero Coupon Bond Duration: ", duration)

price = -npf.pv(rate = 0.03, nper = 10, pmt = 3, fv = 100)
price_up = -npf.pv(rate = 0.04, nper = 10, pmt = 3, fv = 100)
price_down = -npf.pv(rate  = 0.02, nper = 10, pmt = 3, fv = 100)

# Calculate duration using the formula and print result
duration = (price_down -price_up)/(2*price*0.01)
print("Coupon Paying Bond Duration: ", duration)

# Find & print duration of 20 year bond with 3% coupon & 5% yield
price_20y = -npf.pv(rate=0.05, nper=20, pmt=3, fv=100)
price_up_20y = -npf.pv(rate=0.06, nper=20, pmt=3, fv=100)
price_down_20y = -npf.pv(rate=0.04, nper=20, pmt=3, fv=100)
duration_20y = (price_down_20y -price_up_20y)/(2*price_20y*0.01)

print("20 Year Bond: ", duration_20y)

# Create an array of bond yields
bond_yields = np.arange(0, 20, 0.1)

# Convert this array into a pandas DataFrame and add column title
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add bond price column with price varying according to the yield
bond['bond_price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)

# Plot graph of bond yields against prices, add x-axis and y-axis labels, show plot
plt.plot(bond['bond_yield'],bond['bond_price'])
plt.xlabel('Yield (%)')
plt.ylabel('Bond Price (USD)')
plt.show()

# Create array of coupon rates and assign to pandas DataFrame
bond_coupon = np.arange(0,10,0.1)
bond = pd.DataFrame(bond_coupon,columns = ['bond_coupon'])

bond['price'] = -npf.pv(rate = 0.05, nper = 10, pmt = bond['bond_coupon'], fv = 100)
bond['price_up'] = -npf.pv(rate = 0.05+.01, nper = 10, pmt = bond['bond_coupon'], fv = 100)
bond['price_down'] = -npf.pv(rate = 0.05-.01, nper = 10, pmt = bond['bond_coupon'], fv = 100)
bond['duration'] = (bond['price_down'] - bond['price_up'])/(2*bond['price']*0.01)

plt.plot(bond['bond_coupon'],bond['duration'])
plt.xlabel('Coupon (%)')
plt.ylabel('Duration (%)')
plt.show()

# Find the duration of the bond
price = -npf.pv(rate = 0.05, nper = 30, pmt = 3.5, fv = 100)
price_up = -npf.pv(rate = 0.06, nper = 30, pmt = 3.5, fv = 100)
price_down = -npf.pv(rate  = 0.04, nper = 30, pmt = 3.5, fv = 100)
duration = (price_down -price_up)/(2*price*0.01)

# Find the dollar duration of the bond
dollar_duration = price * duration * 0.01
print("Dollar Duration: ", dollar_duration)

# Find the DV01 of the bond
dv01 = price*duration*0.0001
print("DV01: ", dv01)

# Assign DV01 of portfolio and bond to variables
portfolio_dv01 =5000
bond_dv01 = 0.1288
bond_price = 76.94

# Calculate quantity of bond to hedge portfolio
hedge_quantity = portfolio_dv01/bond_dv01
print("Number of bonds to sell: ", hedge_quantity)

# Calculate dollar amount of bond to hedge portfolio
hedge_amount = hedge_quantity*bond_price
print("Dollar amount to sell: USD", hedge_amount)