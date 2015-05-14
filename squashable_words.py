# You want to test whether a word is 'squashable'. What that means is that you want
# to know whether you can subtract 1 letter at a time for a word and still have a word.
# For example, subtracting v from vice gives ice, which is a word. Subtracting e from
# ice gives ic, which is in our dictionary because it is an integrated circuit. 
# Subtracting c from ic gives i, which is a word. Then, we clearly have a word
# that we can call squashable.

word_dict = {'a':'a', 'as':'as', 'ash':'ash', 'i': 'i', 'ic':'ic', 'ice':'ice', 'vice':'vice'}

def find_permutations(word):
	permutations = []
	for i in range(len(word)):
		permutations.append(word[:i] + word[i+1:])
	return permutations

def test_squashable(word, word_dict):
	print(find_permutations(word))
	for subword in find_permutations(word):
		if subword == '':
			return True
		if subword in word_dict:
			return test_squashable(subword, word_dict)
	return False

print(test_squashable('vice', word_dict))