#MCP361
#Assignment 1
#Siddharth Dixit
#2018ME20727

import math

#Set-up time for a production run in minutes
Tsetup = 75

#Setup time per hour
TSetup_hr = Tsetup/60

#Tool Cost in ₹
TCost = 2500

#Tool wear rate
TWear_rate = 0.005

#Lubricating oil required per setup in liters
oilsetup = 0.4

#Lubricating oil costs in ₹ / liter
oilsetupCost = 100

#Salary of the operator in ₹ / hr
salary = 50

#Monthly demand in units
Demand = [100,90,115,120,95,100,90,105,105,100,110,105]

#Total Demand in a year
TotalDemand = sum(Demand)

#Number of working Days per month
NoofWDays = [28,29,30,29,28,29,30,30,30,29,30,31]

#Total Number of working Days
TotalDays = sum(NoofWDays)

#Average demand per month
AvgDemand_month = TotalDemand/12

#Average production per day
AvgProd_day = TotalDemand/TotalDays

#Area of warehouse in sq ft.
WArea = 500

#the manufacturer has rented a warehouse of 500 sq ft. at ₹2 per sq ft per month
WCost = 2

#Electricity charges in ₹ per month
ECost = 100

#Facility maintenance charges in ₹ per month
MCost = 100

#Amount stored each month in units
Amt = 500

#Production cost per unit in ₹
PCost = 15

#Shortage Cost in ₹
ShortageCost = 5

#Overage Cost in ₹
OverageCost = 2

#Oil cost per setup
CostOil_setup = oilsetup * oilsetupCost

#Tool cost per set up
TCost_setup = TCost * TWear_rate * TSetup_hr

#Operating Cost per set up
OC_setup = salary * TSetup_hr

#Total Setup cost per setup(Sum of above 3)
TotalSetupCost_setup = CostOil_setup + TCost_setup + OC_setup

#Warehouse cost per month in ₹
WarehouseCost_month = WArea * WCost

#Total inverntory cost per month in ₹
TotalInventoryCost_month = WarehouseCost_month + ECost + MCost

#Total inverntory cost for 12 monnths in ₹
TotalInventoryCost = TotalInventoryCost_month * 12

#Optimal Lot Size
a = TotalInventoryCost_month/500
b = 2 * AvgDemand_month * TotalSetupCost_setup
LotSize = round(math.sqrt(b/(a)),0)
NumberOfSetups = round(TotalDemand/LotSize)

#Total setup cost
TotalSetupCost = TotalSetupCost_setup * NumberOfSetups

#Production per month
Prod_month = [round(AvgProd_day * i) for i in NoofWDays] #while loop

#Total Production cost
TotalProdCost = sum(Prod_month) * PCost

#Inventory, Overage & Shortage for 12 months

Inventory = [0]
Overage = [max(Prod_month[0] - Demand[0], 0)]
Shortage = [max(Demand[0] - Prod_month[0], 0)]

j = 1
while j < 12 :
    Overage.append(max(Prod_month[j] - Demand[j], 0))
    Shortage.append(max(Demand[j] - Prod_month[j] - Inventory[j - 1], 0))
    if (Demand[j] > Prod_month[j]):
        Inventory.append(max(Inventory[j - 1] - Demand[j] + Prod_month[j], 0))
    else:
        Inventory.append(Inventory[j - 1] + Overage[j])
    j = j + 1

#Total Overage Cost
TotalOverageCost = OverageCost * Inventory[11]

#Total Shorage Cost
TotalShortageCost = sum(Shortage) * ShortageCost

print('Total production cost is',TotalProdCost)
print('Inventory cost is',TotalInventoryCost)
print('Set-up cost is',TotalSetupCost)
print('Shortage cost is',TotalShortageCost)
print('Overage cost is',TotalOverageCost)









