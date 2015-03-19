# #this algorithm works by perpetually moving an element back in the list by comparing
# #it to every element in the subsorted part of the list (the start)
# #it moves all of the smaller elements forward and then inserts the new value at the
# #correct point.
def insertion_new_list(lst):
	lst_sorted = [lst[0]]
	for j in range(1,len(lst)):
		for i in range(len(lst_sorted)):
			if lst_sorted[i] > lst[j]:
				lst_sorted.insert(i, lst[j])
				break
			elif i == len(lst_sorted)-1:
				lst_sorted.append(lst[j])
		print(lst_sorted)
	return lst_sorted

# print(insertion_new_list([5,2,4,6,1,3]))

def insertion_mutate(lst):
	for j in range(1,len(lst)):
		key = lst[j]
		i = j-1
		print(lst)
		while i >= 0 and lst[i] > key:
			print('switching:', lst[i+1],'to',lst[i])
			lst[i+1] = lst[i]
			print(lst,i)
			i = i-1
			print('i is now:', i)
		lst[i+1] = key
	return lst
print(insertion_mutate([5,2,4,6,1,3]))

def selection(lst):
	new_lst = list(lst)
	returnlst = []
	while new_lst:
		smallest = min(new_lst)
		returnlst.append(smallest)
		small_index = new_lst.index(smallest)
		new_lst.pop(small_index)
	return returnlst
print(selection([5,2,4,6,1,3]))
#quicksort:
def partition(lst):
	if len(lst) <= 1:
		return 0,lst
	pivot = len(lst)//2
	pivot_val = lst[pivot]
	high = len(lst)-1
	lst[pivot],lst[high] = lst[high],lst[pivot]
	for i in range(high):
		if lst[i] > pivot_val:
			for j in range(i,high):
				if lst[j] < lst[i] and lst[j] < pivot_val:
					lst[i],lst[j]=lst[j],lst[i]
	final_pivot = high
	for i in range(high):
		if lst[i] > pivot_val:
			lst[i],lst[high] = lst[high],lst[i]
			final_pivot = i
			break
	return final_pivot,lst
def quick_sort(lst,low,high):
	#find pivot first. we pick the middle of the list.
	#smaller will be to the left. bigger to the right.
	if low >= high or lst == []:
		return lst
	split,ordered = partition(lst)
	return quick_sort(ordered[0:split],low,split-1)+[ordered[split]]+quick_sort(ordered[split+1:],split+1,high)

testlst = [1,2,3]
testlst = quick_sort(testlst,0,len(testlst)-1)
print(testlst, len(testlst))
#mergesort:
def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    if len(lst1) == 0 and len(lst2) == 0:
        return []
    elif len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    if lst1[0] <= lst2[0]:
        return [lst1[0]] +  merge(lst1[1:], lst2)
    elif lst2[0] < lst1[0]:
        return [lst2[0]] + merge(lst1, lst2[1:])

def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    if len(seq) == 1 or len(seq) == 0:
        return seq
    half_index = len(seq)//2
    return merge(mergesort(seq[:half_index]),mergesort(seq[half_index:]))
