file_loc = "E:\Desktop\presentations\Posets\covers.txt"
with open(file_loc) as f:
    L = f.readlines()
L = [L[i].split() for i in range(len(L))]
#print L
"""
number of nodes
number of cover relations
height
"""
nn = int(L[0][0]) 			# number of nodes
nc = int(L[1][0])			# number of cover relations
height = int(L[2][0]) 		# self explan.
cov = {i:[] for i in range(nn)}
for i in range(3, 3+nc):
	key = int(L[i][0])
	val = int(L[i][1])
	cov[key].append(val)
#print cov

hor = 0.5
ver = 0.5
short = -6

print "\\begin{tikzpicture}"
print "\t\\def \\hor{", hor, "};"
print "\t\\def \\ver{", ver, "};"
print "\t\\def \\short{", short, "};"

for h in range(height):
	V = L[-(h+1)][0]
	#print V
	for i in range(len(V)):
		if V[i] == '*':
			continue
		print "\t\\node ("+str(V[i])+") at ("+str(i)+"*\\hor,"+str(h)+"*\\ver) {};"
		print "\t\\draw[fill=black] ("+str(i)+") circle (.3ex);"

for i in cov:
	C = cov[i]
	for y in C:
		print "\t\\draw[shorten <= \\short, shorten >= \\short] ("+str(i)+ ") -- ("+str(y)+");"

print "\\end{tikzpicture}"