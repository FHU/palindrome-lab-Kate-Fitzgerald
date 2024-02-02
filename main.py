#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.strip()
    word = word.upper()
    if word.isalpha() == True:
        reverse_word = word[::-1]
        if reverse_word == word:
            return True
        else:
            return False
    else:
        return False

#YOUR CODE GOES HERE
print(palindrome(input()))