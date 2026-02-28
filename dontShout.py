inpt=input("Enter Sentence here: ")
words=inpt.split()

valid_words=[]

for word in words:
    if not word.isupper():
        valid_words.append(word)

output=' '.join(valid_words)
print(output)