#MCP361
#Assignment 3
#Problem 1
#Siddharth Dixit
#2018ME20727

#Assumption : a planning horizon of 8 time periods for this exercise
#input demand over the planning horizon
#Demand (units)
Demand = [15, 20, 30, 10, 30, 30, 30, 30]

#Available on-hand inventory
AvailableInventory = 30

#Scheduled receipts
SReceipts = [20,10,5]

def MRP(Demand,SReceipts,AvailableInventory):
    n = len(Demand)
    #Initializing the solution
    NetReq = []
    for i in range(n):
        NetReq.append(0)

    #Calculating the Net Requirement
    i = 0
    while i < n:
        if Demand[i] <= AvailableInventory:
            #Requirement is Zero
            #AvailableInventory - Demand
            AvailableInventory = AvailableInventory - Demand[i]
            i = i + 1
        else:
            if len(SReceipts)==0:
                NetReq[i] = Demand[i] - AvailableInventory
                #AvailableInventory is Zero
                AvailableInventory = 0 
                i = i + 1
            else:
                AvailableInventory = AvailableInventory + SReceipts[0]
                del SReceipts[0]

    print("Final net requirements for the planning horizon = ", NetReq)
    return NetReq

MRP(Demand,SReceipts,AvailableInventory)
