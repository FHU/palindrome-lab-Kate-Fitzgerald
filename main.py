#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.strip()
    word = word.upper()
    words = word.split()
    newword = "".join(words)

    if newword.isalpha() == True:
        reverse_word = newword[::-1]
        if reverse_word == newword:
            return True
        else:
            return False
    else:
        return False

#YOUR CODE GOES HERE
user = input()
print(palindrome(user))