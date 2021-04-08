# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character 
# appears only once in the original string, or ")" if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.


def duplicate_encode(word):

    word = word.lower()

    parentheses = ""

    for i in word:
        qtd = word.count(i)
        if qtd > 1:
            parentheses += ")"
        else:
            parentheses += "("
    
    return parentheses

n = duplicate_encode('Success')
print(n)