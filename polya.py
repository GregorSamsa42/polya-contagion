import random

def append(x,y):
	r = random.randint(1, x+y)
	if r > x:
		return (x,y+1)
	if r <= x:
		return (x+1,y)
    
def polya(n):
	(p,q) = (1,1);
	for x in range(1, n):
		(p,q) = append(p,q);
	print(ratio(p,q));
	
def polyac():
	(p,q) = (1,1);
	while True:
		(p,q) = append(p,q);
		print(ratio(p,q));
