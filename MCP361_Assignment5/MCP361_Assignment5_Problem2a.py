# MCP361 : Assignment 5
# Siddharth Dixit
# 2018ME20727
# Problem 2a
import pulp as p 

# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Maximization of Profits', p.LpMaximize) 

# Creating problem Variables (16 Decision variables)
#Heavy-duty
p1_HeavyD = p.LpVariable("p1_HeavyD", lowBound = 0, cat='Integer')
p2_HeavyD = p.LpVariable("p2_HeavyD", lowBound = 0, cat='Integer') 
p3_HeavyD = p.LpVariable("p3_HeavyD", lowBound = 0, cat='Integer')

#Standard
p1_Standard = p.LpVariable("p1_Standard", lowBound = 0, cat='Integer')
p2_Standard = p.LpVariable("p2_Standard", lowBound = 0, cat='Integer') 
p3_Standard = p.LpVariable("p3_Standard", lowBound = 0, cat='Integer')

#Economy
p1_Economy = p.LpVariable("p1_Economy", lowBound = 0, cat='Integer')
p2_Economy = p.LpVariable("p2_Economy", lowBound = 0, cat='Integer') 
p3_Economy = p.LpVariable("p3_Economy", lowBound = 0, cat='Integer')

#Profits = [Heavy-duty, Standard, Economy]
Profits = [12, 10, 7]

#Lead Requirements = LeadR
#LeadR = [Heavy-duty, Standard, Economy]
LeadR = [21, 17, 14]

# Objective Function 
Lp_prob += Profits[2]*(p1_Economy + p2_Economy + p3_Economy)+ Profits[1]*(p1_Standard + p2_Standard + p3_Standard) + Profits[0]*(p1_HeavyD + p2_HeavyD + p3_HeavyD)


Lp_prob += p1_HeavyD + p1_Standard + p1_Economy <= 550
Lp_prob += p2_HeavyD + p2_Standard + p2_Economy <= 750
Lp_prob += p3_HeavyD + p3_Standard + p3_Economy <= 225

Lp_prob += LeadR[0]*p1_HeavyD + LeadR[1]*p1_Standard + LeadR[2]*p1_Economy <= 10000
Lp_prob += LeadR[0]*p2_HeavyD + LeadR[1]*p2_Standard + LeadR[2]*p2_Economy <= 7000
Lp_prob += LeadR[0]*p3_HeavyD + LeadR[1]*p3_Standard + LeadR[2]*p3_Economy <= 4200

Lp_prob += p1_HeavyD + p2_HeavyD+p3_HeavyD <= 700
Lp_prob += p1_Standard + p2_Standard + p3_Standard <= 900
Lp_prob += p1_Economy + p2_Economy + p3_Economy <= 450

status = Lp_prob.solve() # Solver 


print("3x3 allocation matrix:")
print()

x1=[p1_HeavyD.value(), p1_Standard.value(), p1_Economy.value()]
x2=[p2_HeavyD.value(), p2_Standard.value(), p2_Economy.value()]
x3=[p3_HeavyD.value(), p3_Standard.value(), p3_Economy.value()]

print("       Heavy-duty, Standard, Economy")
print("Plant 1", x1)
print("Plant 2", x2)
print("Plant 3", x3)
print()

print ("Profit = ₹", end=" ")
print(p.value(Lp_prob.objective)) 
# Printing the final solution 

