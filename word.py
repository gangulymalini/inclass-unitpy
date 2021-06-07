def wordtester(word):
    count = 0
    for i in range(0, len(word)):
        if (word[i] == " "):
            count = count + 1
    
    return(count + 1)


