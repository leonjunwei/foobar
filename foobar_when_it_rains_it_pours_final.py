def rightCompare(heights,index): #returns True only if the rightmost index is lower
    if index == len(heights)-1:
        return False
    elif heights[index+1]>=heights[index]:
        return False
    else:
        return True

def rightBank(heights,index): #returns 200000 if there isn't another index to the right with the same height, 
                              #returns the closest right bank of the pond otherwise -> 2-1-3 should give the index of 3
    nextRight=0
    nextRight=(next((k for k in xrange(index+1,len(heights)) if heights[k] >= heights[index]),200000))
    return nextRight
    # if nextRight == 200000:
    #     return 200000
    # else:
    #     return nextRight
#We can probably just return nextRight.

def rightAdd(heights,array): #array is a [startindex, stopindex, count] list - it doesn't count the stopindex.
    count = array[2]
    for i in xrange(array[0],array[1]):
        count+=heights[array[0]]-heights[i]
    array[2] = count
    return array


def toTheRightCalc(heights,array): #array is a list of [index toTheRightCalc starts from, count thus far]
    index = array[0]
    if index == len(heights)-1 or index == len(heights)-2:
        return array
    else:
        a = max(heights[index+1:len(heights)])
        count = array[1]
        localRightMaxIndex = next(k for k in xrange(index+1,len(heights)) if heights[k] == a) #gives the index of the local leftward maximum

        if localRightMaxIndex == index+1:
            array[0] = localRightMaxIndex
            array[1] = count
            return array
        else:

            for m in xrange(index+1,localRightMaxIndex):
                count+=(a-heights[m])
            array[0] = localRightMaxIndex
            array[1] = count    
            return array


def answer(heights):
    """This function takes in a list of differently-heighted crates and calculates the amount of water that'd be trapped between them."""
    x=0
    count = 0
    count_2=0
    count_3=0
    index = 0
    maxHeightIndexList = []
    maxHeight=max(heights)
    for i in xrange(0,len(heights)): #stores indices of max heights
        if heights[i] == maxHeight:
            maxHeightIndexList.append(i)
    # print "max height list " + str(maxHeightIndexList)
    firstMaxHeight = maxHeightIndexList[0]
    if len(maxHeightIndexList)==1:
        firstMaxHeightIndex = maxHeightIndexList[0]
        lastMaxHeightIndex = maxHeightIndexList[0]

    else:
        firstMaxHeightIndex = maxHeightIndexList[0]
        lastMaxHeightIndex = maxHeightIndexList[len(maxHeightIndexList)-1]

    a = []

    while index<firstMaxHeightIndex and x<10000:
        if rightCompare(heights,index) and rightBank(heights,index)<10000:
            a = rightAdd(heights,[index,rightBank(heights,index),count])
            count = a[2]
            index = rightBank(heights,index)
            x+=1
        else:
            index+=1

    else:
        while index>=firstMaxHeightIndex and index<lastMaxHeightIndex and x<10000:
            a = rightAdd(heights,[firstMaxHeightIndex,lastMaxHeightIndex,count_2])
            count_2 = a[2]
            index = a[1]
            x+=1
            # print "count2" + str(count_2)
        else:
            array = [index,count_3]
            # print array
            while array[0]<len(heights)-1 and x<10000:
                array = toTheRightCalc(heights,array)

                count_3 = array[1]
                x+=1
            
    return count+count_2+count_3

heights = [1,2,4,3,5,2,4,2,1,7]


print answer(heights)