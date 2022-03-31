#MCP361
#Assignment 3
#Problem 2
#Siddharth Dixit
#2018ME20727


#Wagner-Whitin code(From Assignment 2)
def fill_list_with_list_of_zeroes(list1,n):
    list_of_zeroes=[]
    for i in range(0,n):
        list_of_zeroes.append(0)
    for i in range(0,n):
        list1.append(list_of_zeroes.copy())

    

def solve(SetupCost, HoldingCost, Demand):

    #Number of periods = n
    n = len(Demand)
    Cost_Production = []
    table = []
    fill_list_with_list_of_zeroes(Cost_Production,n)
    fill_list_with_list_of_zeroes(table,n)

    for i in  range(0,n):
        for j in range(i,n):
            Cost_Production[i][j]=SetupCost
            for l in range(i+1,j+1):
                Cost_Production[i][j]+= HoldingCost*(l-i)*Demand[l]
    
    OptimalCost_Prod=[]
    fill_list_with_list_of_zeroes(OptimalCost_Prod,n)
    # Initializing the optimal order cost
    # Row is the starting period of production
    # Column is the ending period of production
    matrix_of_orders = [[[j] for i in range(0,n)] for j in range(0, n)]
    i=0
    while i < n:
        j = 0
        while j < i + 1:
            OptimalCost_Prod[i-j][i]=Cost_Production[i-j][i]
            #starting period is i-j
            #ending period is i

            #below loop will add further cost from i-j to j period
            if i - j == 0:
                    table[i-j][i] = Cost_Production[i-j][i]
            l=i-j
            while l<i:
                temp_cost = Cost_Production[i-j][l] + OptimalCost_Prod[l+1][i]
                #producing in the start till i - j
                #optimal cost from (i-j+1) which is l to i
                if i - j == 0:
                    table[l][i]=Cost_Production[l][i]
                    if l>0:
                        table[l][i]+=OptimalCost_Prod[0][l-1]
                if (temp_cost< OptimalCost_Prod[i-j][i]): 
                    OptimalCost_Prod[i-j][i] = temp_cost #if the cost is less than current optimal cost, it needs to be updated
                    matrix_of_orders[i-j][i] = [i-j, l+1] #updating the matrix of orders
                l=l+1
            j=j+1
        table[i][i]=OptimalCost_Prod[0][i-1]+SetupCost
        i=i+1
    optimal_cost = OptimalCost_Prod[0][n-1]
    PeriodOfOrders = periods(matrix_of_orders,n)
    order = production_amount(PeriodOfOrders, Demand)
    p = len(PeriodOfOrders)
    i = 0
    while i < p:
        PeriodOfOrders[i] += 1
        i = i + 1
    """print()
    print("Matrix represents table 2.4 from the book Factory Physics")
    print()
    print ("Table 2.4")
    print()
    for i in range(0,n):
        for j in range(0,n):
            print(table[i][j], end=" ")
            if j<i:
                print(" ", end=" ")
        print()
    k=len(PeriodOfOrders)
    i=0
    while i<k:
        PeriodOfOrders[i]=PeriodOfOrders[i]+1
        i=i+1

    print()
    print ("Optimal Answer")
    print("Order Periods are", PeriodOfOrders)
    print()
    print ("Optimal cost of production = $", optimal_cost)
    print()
    print ("Order amount for each period :-")
    print(order)"""
    return optimal_cost, order, PeriodOfOrders

def production_amount(PeriodOfOrders, Demand):
    n = len(Demand)
    order = [0]*n
    l = len(PeriodOfOrders)
    i = 0
    while i < l:
        start=PeriodOfOrders[i]
        if i!=l-1:
            end=PeriodOfOrders[i+1]
        else:
            end = n + 1
        order[start]=sum(Demand[start:end])
        i = i + 1
    return order

#Periods which need to order
def periods(matrix_of_orders, n):
    order = [0]
    next_production=0
    while(len(matrix_of_orders[next_production][n-1])==2):
        order.append(matrix_of_orders[next_production][n-1][1])
        next_production = matrix_of_orders[next_production][n-1][1]
    return order

#Setup cost of INR 100 per production run
SetupCost=100

#holding cost of INR 1.00 per unit per month
HoldingCost=1

AllPeriodDemand = [20, 50, 10, 50, 50, 10, 20, 40, 20, 30]

solve(SetupCost, HoldingCost, AllPeriodDemand)


#MRP code from Problem 1 of this Assignment 3
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

NetReq = MRP(Demand,SReceipts,AvailableInventory)

DemandNetReq = []

n = len(NetReq)
i = 0
initial = 0
count = 0 
while i < n:
    if NetReq[i]==0 and initial==0:
        i = i + 1
        count = count + 1
    else:
        c = NetReq[i]
        initial = 1
        DemandNetReq.append(c)
        i = i + 1


if sum(NetReq)==0: #No order is needed
    print("The onhand Inventory and SRs are enough to cater to the demand. No new order has to be placed")

else:
    optimal_cost, solution, new_period = solve(SetupCost,HoldingCost,DemandNetReq)
    i = 0
    while i < len(new_period):
        new_period[i] = new_period[i] + count
        i = i + 1
    for i in range(count):
        solution.insert(0,0)

    print()
    print("Order Periods :", new_period)
    print()
    print ("The optimal cost of production is INR",optimal_cost)
    print()
    print ("The order amount for each period :",solution)



