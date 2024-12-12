import re
str = input() # "the quick fox"
tokens = str.split(" ")
# ["the", "quick", "fox"]
token_val = 0
#print(tokens)

# this scanner is a hastable / dictionary & finite state machine 
append = ""
tokenized = []
for token in tokens:
	match = re.search(r"\d", token) # check if its a number
	if match == None: # not a number
		if token == "if":
			token_val = 1
		if token == "else:":
			token_val = 2
		if token == "elif:":
			token_val = 4
		if token == "+":
			token_val = 5
		if token == "-":
			token_val = 6
		#if token == str: #raw text shouldn't be before an =
			#token_val = 3
		if token_val < 1: # not anything we are looking for
			append = append + token + " "
		else:
			if (len(append) > 0): 
				tokenized.append(append)
			tokenized.append(token_val)
			append = ""
			token_val = 0
	else: # is a number
		if (len(append) > 0): 
			tokenized.append(append)
			append = ""
		token_val = 3
		tokenized.append(token_val)
		token_val = 0

#append = " " + append
if (len(append) > 0):
	tokenized.append(append)

def getToken(tokenized, i):
	return tokenized[i+1] # return next in array

#print(token_val)
#print(tokenized)
i = -1
while i < len(tokenized)-1:
	print(getToken(tokenized,i))
	i = i + 1