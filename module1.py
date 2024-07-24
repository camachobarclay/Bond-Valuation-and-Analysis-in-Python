#simple interest 
import numpy_financial as npf

pv = 1000
r = 0.05
n = 12
interest = pv*r*n

print(interest)

fv = pv+ interest
print(fv)

# compound interest
fv = pv*(1+r)**n
print(fv)

###################

deposit_fv = 1000*(1+0.03)**3
topup_1_fv = 100*(1+0.03)**2
topup_2_fv = 100*(1+0.03)**1
topup_2_fv = 100

print(deposit_fv + topup_1_fv+topup_2_fv+topup_3+fv)

print(deposit_fv + topup_1_fv+topup_2_fv+topup_3+fv - (1000+300))

#?nppf.fv

totalval = npf.fv(rate = 0.03, nper = 3, pmt = -100, pv = -1000)

# Using annual compounding frequency

npf.fv(rate = 0.05, nper = 10, pv = -1000)

# Using monthly compounding frequency
npf.fv(rate = 0.05/12, nper = 10*12, pmt = 0, pv = -1000)

# Using daily compounding frequency
npf.fv(rate = 0.05/365, nper = 10*365, pmt = 0, pv = -1000)

###################
#?npf.nper

npf.nper(rate = 0.05/12, pmt = -270, pv = 0, fv = 7000)

#?npf.pmt

npf.pmt(rate = 0.035/12, nper = 10*12, pv = 275000, fv = 0)

#npf.rate

12*npf.rate(nper = 30*12, pmt = -1500, pv = 0, fc = 1000000)


############################


# Assign present value, rate and number of periods
pv = 10000
r = 0.03
n = 10

# Calculate total amount of simple interest earned
simple_interest = pv*r*n
print(simple_interest)

# Calculate value of the savings account
fv = pv + simple_interest
print(fv)

# nicole zakiyan
# mateus lima  
# rajesh 

# Assign present value, rate and number of periods
pv = 10000
r = 0.03
n = 10

# Calculate the value of the savings account
fv = pv*(1+r)**n
print(fv)

# Calculate the total amount of compound interest earned
compound_interest = fv - pv
print(compound_interest)

##

# Import numpy_financial package using the alias npf
import numpy_financial as npf

# Calculate the future value of an investment
savings = npf.fv(rate=0.05, nper=30, pmt=-5000, pv=-10000)

# Print the result
print(savings)

##

# Calculate and print the growth of USD 10,000 invested in the first account
account_1 = npf.fv(rate=0.05, nper=10, pmt=0, pv=-10000)

# Calculate and print the growth of USD 10,000 invested in the second account
account_2 = npf.fv(rate=0.045/12, nper=10*12, pmt=0, pv=-10000)

# Calculate the growth of USD 10,000 invested in the third account
account_3 = npf.fv(rate = 0.049/365, nper = 10*365, pmt = 0, pv = -10000)

# Print the value of the third savings account
print(account_3)

##

### Import numpy_financial package using alias npf

import numpy_financial as npf

# Calculate how long it will take to reach the savings goal
number_periods = npf.nper(rate = 0.045/4, pmt = -1250, pv = 0, fv = 30000)

# Print the result
print(number_periods)

# Import the numpy_financial package using the alias npf
import numpy_financial as npf

# Calculate monthly payment required
required_payment = npf.pmt(rate = 0.035/12, nper = 20*12, pv = 275000, fv = 0)


# Print the result
print(required_payment)

# Import the numpy_financial package using the alias npf
import numpy_financial as npf

# Calculate return on investments required: required_return

required_return = 12*npf.rate(nper = 30*12, pmt = -1500, pv = 0, fv = 2000000)


# Print the result
print(required_return)

# Calculate how much USD 100 per month compounding at 3% grows to after 5 years
total_savings = npf.fv(rate=0.03/12, nper=5*12, pmt=-100, pv=0)
print(total_savings)

# Calculate the time to reach a USD 15,000 deposit on a house
time_to_goal = npf.nper(rate=0.05/12, pmt=-250, pv=-5000, fv=15000)
print(time_to_goal)

# Calculate the monthly contributions needed to retire with USD 1,000,000
monthly_contributions = npf.pmt(rate=0.05/12, nper=(65-22)*12, pv=0, fv=1000000)
print(monthly_contributions)