#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.strip()
    word = word.upper()
    word = word.split()
    for i in word:
        newword = str(word).strip
    newword = "".join(word)

    
    if newword.isalpha() == True:
        reverse_word = newword[::-1]
        if reverse_word == newword:
            return True
        else:
            return False
    else:
        return False

#YOUR CODE GOES HERE
print(palindrome(input()))