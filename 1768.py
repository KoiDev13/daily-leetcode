# word1 = "abc"
# word2 = "pqr"
word1 = "ab" 
word2 = "pqrs"

nword = ""
i = 0 

while i < len(word1) or i < len(word2):
    if i < len(word1):
        nword += word1[i]
    if i < len(word2):
        nword += word2[i]
    i += 1

print(nword)