def palindrome(string):
	"""
	This function checks whether a string is palindrome or not
	
	Args: String which you want to check
	
	Returns: True or False
	"""
	end = len(string)-1
	for i in range(len(string)//2):
		if string[i]!=string[end]:
			return False
		end-=1
	return True
	
print(palindrome("abba"))
print(palindrome("banana"))
		
