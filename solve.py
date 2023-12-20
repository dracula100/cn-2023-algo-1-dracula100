remove_bracket = lambda n:n[:len(n)-1][1:]

child,candy = (int(input()) for x in "22")

client = [input().split() for x in range(child)]
client = {x[0]:remove_bracket(x[1]).split(",") for x in client}


candy_list = [input().split() for x in range(candy)]
candy_list = {x[0]:int(remove_bracket(x[1])) for x in candy_list}

"""
file = open("example_input.txt","r")
child,candy = (int(file.readline()) for x in "22")
client = [file.readline().split() for x in range(child)]
client = {x[0]:remove_bracket(x[1]).split(",") for x in client}
candy_list = [file.readline().split() for x in range(candy) ]
candy_list = {x[0]:int(remove_bracket(x[1])) for x in candy_list}
file.close()
"""
print(client)
print(candy_list )
res = {}
for x in candy_list :
	s = candy_list[x]//[e for i in list(client.values()) for e in i].count(x)
	selected = [i for i in client if x in client[i]]
	for i in selected:
		if i not in list(res.keys()):res[i]={}
		res[i][x] = s

for x in res:
	t = ",".join(i+" ("+str(res[x][i])+")" for i in res[x])
	print(x+" : "+t)
