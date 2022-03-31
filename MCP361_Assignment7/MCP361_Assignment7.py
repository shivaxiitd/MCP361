# MCP361 : Assignment 7
# Siddharth Dixit
# 2018ME20727

import numpy as np

def NashE(text_file) :
	txt_file = open(text_file + ".txt", "r")
	my_list = [line.rstrip('\n') for line in txt_file]
	Row = len(my_list)
	Column = len(my_list[0].split(";"))
	player1 = np.zeros((Row,Column))
	player2 = np.zeros((Row,Column))
        
	for i in range(Row):
		list_new = my_list[i].split(";")
		for j in range(Column):
			Strategy = list_new[j].split(",")
			player1[i][j] = Strategy[0]
			player2[i][j] = Strategy[1]

	final = []
	for i in range(Row):
		for j in range(Column):
			Strategy1 = player1[i][j]
			Strategy2 = player2[i][j]
			if Strategy1 == np.max(player1, axis=0)[j]:
				if Strategy2 == np.max(player2, axis=1)[i]:
					final.append("{} {}".format(i+1,j+1))

	print(text_file)
	if final != [] :
		for line in final :
			i,j = line.split(" ")
			print("Player 1 plays its Strategy {} and Player 2 plays its Strategy {}".format(i,j)) #Format taken from problem PDF
	else :
		print("No equilibrium")


print("Result for problem 1:")
NashE("MCP361_2018ME20727_Assignment7_Problem1")
print()
print()
print("Result for problem 2:")
NashE("MCP361_2018ME20727_Assignment7_Problem2")
print()
print()
print("Result for problem 3:")
NashE("MCP361_2018ME20727_Assignment7_Problem3")
print()
print()
print("Result for problem 4:")
NashE("MCP361_2018ME20727_Assignment7_Problem4")
print()
print()
print("Result for problem 5:")
NashE("MCP361_2018ME20727_Assignment7_Problem5")
print()
print()
print("Result for problem 6:")
NashE("MCP361_2018ME20727_Assignment7_Problem6")







