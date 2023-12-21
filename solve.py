remove_bracket = lambda n:n[:len(n)-1][1:]
# My model of input (from stdin ) here is like this:
"""
	2
 	2
  	Alice (Chocolate,Guimauve)
   	Bob (Pecto,Jok)
    Chocolate (10)
    Pecto (30)
"""

candy_list = {}
client = {}

def fromFile():
	global candy_list,client
	file = open("example_input.txt","r")
	kid,candy = (int(file.readline()) for x in "22")
	client = [file.readline().split() for x in range(kid)]
	client = {x[0]:remove_bracket(x[1]).split(",") for x in client}
	candy_list = [file.readline().split() for x in range(candy) ]
	candy_list = {x[0]:int(remove_bracket(x[1])) for x in candy_list}
	file.close()

def fromStdin(): # If we choose to get input from stdin
	global client , candy_list
	kid,candy = (int(input()) for x in "22")
	client = [input().split() for x in range(kid)]
	client = {x[0]:remove_bracket(x[1]).split(",") for x in client}
	candy_list = [input().split() for x in range(candy)]
	candy_list = {x[0]:int(remove_bracket(x[1])) for x in candy_list}

def setExample(): # Directly from the code 
	global client , candy_list
	client = {
		"Alice" : ("Chocolat","Guimauve"),
		"Bob" : ("Caramel","Fruits"),
		"Charlie" : ("Chocolat","Caramel"),
	}
	candy_list = {
		"Chocolat":10,
		"Caramel":8,
		"Guimauve":5,
		"Fruits":6,
	}

setExample()
res = {}

###Solving
for candy in candy_list :
	s = candy_list[candy]//[e for pref_candy in list(client.values()) for e in pref_candy].count(candy)
	if(not s):continue # If the candy is not enough each kid won't have one
	selected = [kid for kid in client if candy in client[kid]]
	for kid in selected:
		if kid not in list(res.keys()):res[kid]={}
		res[kid][candy] = s
###Solving

### View the result
for x in client:
	distribution = ""
	if(x in res):
		distribution = ",".join(i+" ("+str(res[x][i])+")" for i in res[x])
	print(x + " : "+distribution)
