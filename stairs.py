###################################################################################
#You have stairs with N number of steps. You can take either one step steps or two# 
#step steps. How many ways can you climb the stairs?                              #
###################################################################################
def stairs(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	return stairs(n-1) + stairs(n-2)
stairs = count(stairs)
print(stairs(20))
print('call count: ',stairs.call_count, 2 ** 20)