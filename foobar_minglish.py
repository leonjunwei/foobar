words = ["ba", "ab", "cb"]

words1 = ["ba", "ab", "cb" ,"def", "dfg", "gx", "gb", "ghi"]

words2 = ["y", "z", "xy"]

def strip_duplicates(lst): #given a list of words, generates a list of letters in the words
    existingLetters = []
    for i in lst:
        for c in i:
            if c not in existingLetters:
                    existingLetters.append(c)
    return existingLetters

def answer(words):
    letterList = []
    for i in words:
        for c in i:
            letterList.append(c)
    letterList = strip_duplicates(letterList)
    comparisonsList = [] #this should give us a [letter1, letter2, value] where 1 means letter1>letter2 and -1 means letter1<letter2
    for i in range(0,len(words)-1): #comparing the (i)th word with the (i+1)th word
        j=0
        while j<len(words[i]) and j<len(words[i+1]): #comparing letter by letter until we find one that's different
            if words[i][j] != words[i+1][j]:
                if [words[i][j],words[i+1][j],1] not in comparisonsList:
                    comparisonsList.append([words[i][j],words[i+1][j],1])
                break
            j+=1
    # print "comparisonsList = " + str(comparisonsList)
    listAscending = []
    for c in letterList:
        listAscending.append([numSmallerLetters(comparisonsList,c),c])
    result = [x[1] for x in sorted(listAscending)]
    return "".join(result[::-1])

    # print comparisonsList
            
def numSmallerLetters(lst,letter): #given a comparisons list of  [letter1, letter2, value] and a letter, returns the number of letters that have a lower value
    count = 0
    smallerLetters = []
    for c in lst:
        if c[0] == letter:
            count+=(1+numSmallerLetters(lst,c[1])) #i looked online for a recursive way to do the zombies grid problem - recursion is pretty helpful! Although this might be the reason why the program took so long to run.
    return count

print answer(words)
print answer(words1)
print answer(words2)





