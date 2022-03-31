# MCP361 : Assignment 5
# Siddharth Dixit
# 2018ME20727
# Problem 1
import pulp as p 
from pulp import *

# LP Minimization problem 
Lp_prob = p.LpProblem('Minimization of Cost', p.LpMinimize) 

# Creating problem Variables (16 Decision variables) 
x11 = p.LpVariable("x11", lowBound = 0, upBound=1, cat='Integer')
x12 = p.LpVariable("x12", lowBound = 0, upBound=1, cat='Integer') 
x13 = p.LpVariable("x13", lowBound = 0, upBound=1, cat='Integer')
x14 = p.LpVariable("x14", lowBound = 0, upBound=1, cat='Integer')
x15 = p.LpVariable("x15", lowBound = 0, upBound=1, cat='Integer')

x21 = p.LpVariable("x21", lowBound = 0, upBound=1, cat='Integer')
x22 = p.LpVariable("x22", lowBound = 0, upBound=1, cat='Integer') 
x23 = p.LpVariable("x23", lowBound = 0, upBound=1, cat='Integer')
x24 = p.LpVariable("x24", lowBound = 0, upBound=1, cat='Integer') 
x25 = p.LpVariable("x25", lowBound = 0, upBound=1, cat='Integer')

x31 = p.LpVariable("x31", lowBound = 0, upBound=1, cat='Integer')
x32 = p.LpVariable("x32", lowBound = 0, upBound=1, cat='Integer') 
x33 = p.LpVariable("x33", lowBound = 0, upBound=1, cat='Integer')
x34 = p.LpVariable("x34", lowBound = 0, upBound=1, cat='Integer') 
x35 = p.LpVariable("x35", lowBound = 0, upBound=1, cat='Integer')

x41 = p.LpVariable("x41", lowBound = 0, upBound=1, cat='Integer')
x42 = p.LpVariable("x42", lowBound = 0, upBound=1, cat='Integer') 
x43 = p.LpVariable("x43", lowBound = 0, upBound=1, cat='Integer')
x44 = p.LpVariable("x44", lowBound = 0, upBound=1, cat='Integer') 
x45 = p.LpVariable("x45", lowBound = 0, upBound=1, cat='Integer')

x51 = p.LpVariable("x51", lowBound = 0, upBound=1, cat='Integer')
x52 = p.LpVariable("x52", lowBound = 0, upBound=1, cat='Integer') 
x53 = p.LpVariable("x53", lowBound = 0, upBound=1, cat='Integer')
x54 = p.LpVariable("x54", lowBound = 0, upBound=1, cat='Integer') 
x55 = p.LpVariable("x55", lowBound = 0, upBound=1, cat='Integer')

#p1j = [p11, p12, p13, p14, p15]
p1j = [40, 45, 43, 60, 58]

#p2j = [p21, p22, p23, p24, p25]
p2j = [44, 56, 48, 45, 48]

#p3j = [p31, p32, p33, p34, p35]
p3j = [52, 39, 45, 51, 41]

#p4j = [p41, p42, p43, p44, p45]
p4j = [40, 61, 49, 72, 45]

#p5j = [p51, p52, p53, p54, p55]
p5j = [55, 45, 46, 52, 43]


# Objective Function 
Lp_prob += p1j[0]*x11 + p1j[1]*x12 + p1j[2]*x13 + p1j[3]*x14+ p1j[4]*x15+p2j[0]*x21+p2j[1]*x22+p2j[2]*x23+p2j[3]*x24+p2j[4]*x25+p3j[0]*x31+p3j[1]*x32+p3j[2]*x33+p3j[3]*x34+p3j[4]*x35+p4j[0]*x41+p4j[1]*x42+p4j[2]*x43+p4j[3]*x44+p4j[4]*x45+p5j[0]*x51+p5j[1]*x52+p5j[2]*x53+p5j[3]*x54+p5j[4]*x55

Lp_prob +=x11+x12+x13+x14+x15<=1
Lp_prob +=x21+x22+x23+x24+x25<=1
Lp_prob +=x31+x32+x33+x34+x35<=1
Lp_prob +=x41+x42+x43+x44+x45<=1
Lp_prob +=x51+x52+x53+x54+x55<=1

Lp_prob +=x11+x12+x13+x14+x15>=1
Lp_prob +=x21+x22+x23+x24+x25>=1
Lp_prob +=x31+x32+x33+x34+x35>=1
Lp_prob +=x41+x42+x43+x44+x45>=1
Lp_prob +=x51+x52+x53+x54+x55>=1


Lp_prob +=x11+x21+x31+x41+x51<=1
Lp_prob +=x12+x22+x32+x42+x52<=1
Lp_prob +=x13+x23+x33+x43+x53<=1
Lp_prob +=x14+x24+x34+x44+x54<=1
Lp_prob +=x15+x25+x35+x45+x55<=1

Lp_prob +=x11+x21+x31+x41+x51>=1
Lp_prob +=x12+x22+x32+x42+x52>=1
Lp_prob +=x13+x23+x33+x43+x53>=1
Lp_prob +=x14+x24+x34+x44+x54>=1
Lp_prob +=x15+x25+x35+x45+x55>=1
 

status = Lp_prob.solve()


print ("The minimum cost is ₹", end=" ")

print(p.value(Lp_prob.objective)) 
print()
print("Allocation matrix:")

x1 = [p.value(x11),p.value(x12),p.value(x13),p.value(x14),p.value(x15)]
x2 = [p.value(x21),p.value(x22),p.value(x23),p.value(x24),p.value(x25)]
x3 = [p.value(x31),p.value(x32),p.value(x33),p.value(x34),p.value(x35)]
x4 = [p.value(x41),p.value(x42),p.value(x43),p.value(x44),p.value(x45)]
x5 = [p.value(x51),p.value(x52),p.value(x53),p.value(x54),p.value(x55)]

print()

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)


