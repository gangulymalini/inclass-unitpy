def palindrometester(word):
    palin = ""
    for i in range(0, len(word)):
        #print(len(word) - (i+1))
        #print(word[len(word) - (i+1)])
        palin += word[len(word) - (i+1)]
    #print(palin)

    if (palin == word):
        return True
    else:
        return False

#print(palindrometester("you're ugly"))
#print(palindrometester("madam"))