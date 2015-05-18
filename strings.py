#########################################################
# Write a method to return all permutations of a string.#
#########################################################
def string_perms(s):
	if len(s) <= 1:
		return s
	perms = []
	for index in range(len(s)):
		c = s[index]
		for sub_str in string_perms(s[:index]+s[index+1:]):
			perms.append(c+sub_str)
	return perms
string_perms = count(string_perms)
perms = string_perms('this')
print(len(perms), string_perms.call_count, perms)

# GeneratePermutations(na, nb, nc)

# Aab
# Aba
# Baa
# [Aab,Baa,Aba]

def generate_perms1(na,nb,nc):
	word = ‘a’*na + ‘b’*nb + ‘c’*nc
	if len(word) <= 1:
		return word
return permutations(word)
def permutations(s):
	if len(s) <= 1:
		return s
	perms = []
	for index in range(len(s)):
		c = s[index]
		for sub_str in permutations(s[:index]+s[index+1:]):
			perms.append(c+substr)
	return perms

# 1.1
# Implement an algorithm to determine is a string has all unique characters
# Time complexity: O(n) for n being the length of s.
def unique_chars(s):
    letter_distr = {}
    for c in s:
        if c in letter_distr:
            return False
        letter_distr[c] = 0
    return True
# 1.2

def remove_duplicates(s):
	final = ""
	for c in s:
		if c in final:
			continue
		final+=c #Python concatenation is optimized to prevent this from ending up being n^2
	return final
# 1.3
# Given two strings, write a method to decide if a string is permutation of another.
def anagrams(s1,s2):
	if len(s1) != len(s2):
		return False
	distr_1, distr_2 = string_to_dict(s1),string_to_dict(s2)
	for k in distr_1:
		if k in distr_2:
			if distr_1[k] != distr_2[k]:
				return False
		else:
			return False
	return True
def string_to_dict(s):
	letter_distr = {}
	for c in s:
		if c in letter_distr:
			letter_distr[c] += 1
		else:
			letter_distr[c] = 1
	return letter_distr
# 1.4
# Write a method to replace all spacs in a string with '%20'. 
def percent_20(s):
	output = ""
	for c in s:
		if c == ' ':
			output += "%20"
		else:
			output += c
	return output
# 1.5
# Implement a method to perform basic string compression using the counts of the
# repeated characters. Return the original string if the compressed string is not
# shorter than the original string.
# Approach: 
def rle_compress(s):
	count, base, rle_compressed = 0, s[0], ''
	for c in s:
		if c == base:
			count += 1
		else:
			rle_compressed += base + str(count)
			base, count = c, 1
	rle_compressed += base + str(count)
	if len(rle_compressed) >= len(s):
		return s
	return rle_compressed
# Return the character with the maximum number of occurrences
def maxOccurrences(s):
	return max(map(s.count,s))