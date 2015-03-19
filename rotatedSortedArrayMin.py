# Find the minimal number in a rotated sorted array (no duplicates)
# 1 2 3 4 5
# 4 5 1 2 3
# 2 3 4 5 1
def rotated_min(lst):
	pos = 0
	last = len(lst) -1
	while(pos < last):
		mid = (pos + last)//2
		if lst[mid] > lst[last]:
			pos = mid+1
		elif lst[mid] > lst[pos]:
			return lst[pos]
             else:
			last = mid
	return lst[pos]