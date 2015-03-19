"""
Longest Increasing Subsequence Problem
You're given a sequence of characters in the form of a string, where each character is in [a-z].
Your objective is to identify and return the longest possible subsequence of those characters such
that the sequence includes only increasing characters (i.e. each character is greater than the previous
character). The definition of a subsequence is an arbitrary selection of characters from a sequence
such that the relative order of those characters is preserved.

Examples:

lis("abczdef") => "abcdef"
lis("almobcdef") => "abcdef"
lis("axz") => "axz"
lis("xyzabcd") => "abcd"
lis("xzabycd") => "abcd"
lis("xyzab") => "xyz"
lis("xaybd") => "abd"
==================================
"""
def longest_increasing(s, cache = {}):
	roots, results = list(s), []
	if (len(s) <= 1):
		return s
	if (s in cache):
		return cache[s]
	for i in range(len(roots)):
		root = roots[i]
		rest = [c for c in roots[i+1:] if c >= root]
		if len(rest) == 1:
			results.append(root + rest[0])
		results.append(root + longest_increasing("".join(rest), cache))
	all_answers, max_length = [], 0
	for possible in results:
		if len(possible) >= max_length:
			all_answers, max_length = [possible], len(possible)
		elif len(possible) == max_length:
			all_answers.append(possible)
	answer = min(all_answers)
	cache[s] = answer
	return answer
#usage case
print(longest_increasing('string'))

#Original version without dynamic programming.
# def longest_increasing(s):
# 	roots = list(s)
# 	results = []
# 	#added missing base case:
# 	if (len(s) <= 1):
# 		return s
# 	for i in range(len(roots)):
# 		root = roots[i]
# 		#different (reducing roots)
# 		rest = [c for c in roots[i+1:] if c >= root]
# 		if len(rest) == 1:
# 			results.append(root + rest[0])
# 		remaining = "".join(rest)
# 		potential = root + longest_increasing(remaining)
# 		results.append(potential)
# 	answer = []
# 	max_length = 0
# 	for possible in results:
# 		if len(possible) >= max_length:
# 			answer = [possible]
# 			max_length = len(possible)
# 		elif len(possible) == max_length:
# 			answer.append(possible)
# 	return min(answer)