#this code needs optimization
#Author : [ BurhanKhom009 ] Beginner in Python

t = int(input());
loop=1
while loop <=t :
	x=0
	y=0
	maxCordinates = raw_input().split(' ')
	dest = raw_input().split(' ')
	length = int(input())
	s = raw_input()
	for i in range(length):
		if s[i]=='L':
			x = x - 1
		elif s[i]=='R':
			x = x + 1
		elif s[i]=='U':
			y = y + 1
		else:
			y = y - 1
	if x==int(dest[0]) and y==int(dest[1]):
		print "Case %d: REACHED" % loop
	elif x>=0 and y>=0 and x<int(maxCordinates[0]) and y<int(maxCordinates[1]):
		print "Case %d: SOMEWHERE" % loop
	else:
		print "Case %d: DANGER" % loop
	loop+=1

