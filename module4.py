import numpy_financial as npf
import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt

price = -npf.pv(rate = 0.05, nper = 20, pmt = 5, fv = 100)
price_up = -npf.pv(rate = 0.06, nper = 20, pmt = 5, fv = 100)
price_down = -npf.pb(rate  = 0.04, nper = 20, pmt = 5, fv = 100)
duration = (price_down -price_up)/(2*price*0.01)
dollar_duration = duration*price*0.01
print("Bond Price (USD)L ", price)
print("Dollar Duration (USD): ", dollar_duration)

bond_yields = np.arange(0,10,0.1)
bond = pd.DataFrame(bond_yields, columns = ['bond_yields'])
bond['price'] = -npf.pv(rate = bond['bond_yield']/100, nper = 20, pmt = 5, fv = 100)
bond['yield_change'] = bond['bond_yield'] - 5
bond['price_change'] - -100*dollar_duration*bond['yield_change']/100
bond['predicted_price'] = price + bond['price_change']

plt.plt(bond['bond_yield'], bond['price'])
plt.plt(bond['bond_yield'], bond['predicted_price'])
plt.xlabel('Yield (%)')
plt.ylabel('Price (USD)')
plt.title("Actual Bond Prices vs. Predicted Prices Using Duration")
plt.legend(["Actual Price", "Predicted Price"])
plt.legend(["Actual Price", "Preducted Price"])
plt.show()

# 10 year bond with 5% annual coupon and 4% yield to matury has convexity given by
# Pdown + Pup  - 2*P/(P*(delta Y)^2)

price = -npf.pv(rate = 0.04, nper = 10, pmt = 5, fv = 100)
price_up = -npf.pv(rate = 0.05, nper = 10, pmt = 5, fv = 100)
price_down = -npf.pv(rate = 0.06, nper = 10, pmt = 5, fv = 100)
convexity = (price_down + price_up - 2*price)/(price*0.01**2)
print("Convexity: ", convexity)


##########################

price_1= -npf.pv(rate = 0.05, nper = 10, pmt = 0, fv = 100)
price_up_1 = -npf.pv(rate = 0.06, nper = 10, pmt = 0, fv = 100)
price_down_1 = -npf.pv(rate = 0.07, nper = 10, pmt = 0, fv = 100)
convexity_1 = (price_down_1 + price_up_1 - 2*price_1)/(price_1*0.01**2)

price_2= -npf.pv(rate = 0.05, nper = 10, pmt = 10, fv = 100)
price_up_2 = -npf.pv(rate = 0.06, nper = 10, pmt = 10, fv = 100)
price_down_2 = -npf.pv(rate = 0.07, nper = 10, pmt = 10, fv = 100)
convexity_2 = (price_down_2 + price_up_2 - 2*price_2)/(price_2*0.01**2)

print("Low Coupon Bond Convexity: ", convexity_1)
print("High Coupon Bond Convexity: ", convexity_2)

bond_yields = np.arange(0,20,0.1)
bond = pd.DataFrame(bond_yields, columns = ['yields'])

bond['price_10y'] - -npf.pv(rate = bond['yield']/100,
	nper = 10, pmt = 0, fv = 100)
bond['price_30y'] = -npf.pv(rate = bond['yield']/100, 
	nper = 30, pmt = 0, fv = 100)

plt.plt(bond['yield'], bond['price_10y'])
plt.plt(bond['yield'], bond['price_30y'])
plt.xlabel('Yield (%)')
plt.ylabel('Price (USD)')
plt.title("Bond Maturity vs. Convexity")
plt.legend(["10 Year Bond", "30 Year Bond"])
plt.show()

bond_yields = np.arange(0,20,0.1)
bond = pd.DataFrame(bond_yields, columns = ['bond_yields'])

bond['price'] = -npf.pv(rate = bond['bond_yield']/100,
	nper = 10, pmt = 5, fv = 100)

bond['price_up'] = -npf.pv(rate = bond['bond_yield']/100 + 0.01,
	nper = 10, pmt = 5, fv = 100)

bond['price_down'] = -npf.pv(rate = bond['bond_yield']/100 - 0.01,
	nper = 10, pmt = 5, fv = 100)

bond['convexity'] = (bond['price_down'] + bond['price_up'] - 2*bond['price'])/(bond['price']*0.01**2)

plt.plot(bond['bond_yield'], bond['convexity'])
plt.xlabel('Yield (%)')
plt.ylabel('Convexity (%)')
plt.title("Convexity of 10 Year Bond 5% Annual Coupon")
plt.show()

##########################

# Dollar convexity = convesity * bond price *0.01^2

price = -npf.pv(rate = 0.05, nper = 10, pmt = 3, fv = 100)
price_up = -npf.pv(rate = 0.06, nper = 10, pmt = 3, fv = 100)
price_down = -npf.pb(rate  = 0.04, nper = 10, pmt = 3, fv = 100)
convexity = (price_down + price_up - 2*price)/(price*0.01**2)
dollar_convexity = convexity* price*0.01**2
print("Dollar Convexity: ", dollar_convexity)

price = -npf.pv(rate = 0.05, nper = 10, pmt = 3, fv = 100)
price_up = -npf.pv(rate = 0.06, nper = 10, pmt = 3, fv = 100)
price_down = -npf.pb(rate  = 0.04, nper = 10, pmt = 3, fv = 100)

duration = (price_down -price_up)/(2*price*0.01)
dollar_duration = duration*price*0.01

convexity = (price_down + price_up - 2*price)/(price*0.01**2) 
dollar_convexity = convexity* price*0.01**2
convexity_adjustment = 0.5*dollar_convexity*100**2*0.01**2

combined_preduction =  -100*dollar_duration*0.01+ convexity_adjustment
print("Predicted Price Change: ", combined_prediction\\\)
