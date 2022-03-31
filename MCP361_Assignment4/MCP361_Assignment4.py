#MCP361
#Assignment 4
#Siddharth Dixit
#2018ME20727

def MRP(Demand,AvailableInventory, SReceipts):
    n = len(Demand)
    #Initializing the solution
    NetReq = []
    for i in range(n):
        NetReq.append(0)

    #Calculating the Net Requirement
    i = 0
    while i < n:
        if Demand[i] <= AvailableInventory :
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
    return NetReq
Demand_A = [15, 20, 30, 10, 30, 30, 30, 30]
AvailableInventory_A = 30
SReceipts_A = [20, 10]

#Planning Horizon
PH = len(Demand_A)

'''
ABC contains a list with elements in order of A to B, B to C & A to C
=> A to C = 2, A to B = 1, B to C = 1
'''
ABC = [1, 1, 2]


NetReq_A = MRP(Demand_A,AvailableInventory_A,SReceipts_A)

Demand_B = [0]*(PH)

for i in range(PH):
    Demand_B[i]= NetReq_A[i] * ABC[0]

AvailableInventory_B=60
SReceipts_B = [10]

NetReq_B = MRP(Demand_B,AvailableInventory_B,SReceipts_B)

Demand_C=[0]*(PH)

for i in range(PH):
    Demand_C[i]= NetReq_A[i] * ABC[2]


for i in range(len(NetReq_A)):
    Demand_C[i]+= NetReq_B[i] * ABC[1]

AvailableInventory_C = 60
SReceipts_C = [20,10]

NetReq_C = MRP(Demand_C,AvailableInventory_C,SReceipts_C)

print("For production of A, net requirement :", NetReq_A)

print()
print("For production of B, net requirement :", NetReq_B)

print()
print("For production of C, net requirement :", NetReq_C)

print()
print("This output also matches hand written final answer, pasted in PDF named as MCP361_2018ME20727_Assignment4.pdf .")




