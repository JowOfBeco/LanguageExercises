#This code receive user input, a text and a word, and check if
#The word is inside of text field
text = str(input())
word = str(input())

def search(txt, wrd):
    if wrd in txt:
        return "Word found"

    else: return "Word not found" 


print(search(text, word))
