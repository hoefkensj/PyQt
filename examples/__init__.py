l=[]
for i in range(3):
	while not (x:=input()).isnumeric():pass
	if (y:=int(x)) > 0:
		l+=[y*y]
print(sum(l))