# import collections
# import functools

# class memoized(object):
#    '''Decorator. Caches a function's return value each time it is called.
#    If called later with the same arguments, the cached value is returned
#    (not reevaluated).
#    '''
#    def __init__(self, func):
#       self.func = func
#       self.cache = {}
#    def __call__(self, *args):
#       if not isinstance(args, collections.Hashable):
#          # uncacheable. a list, for instance.
#          # better to not cache than blow up.
#          return self.func(*args)
#       if args in self.cache:
#          return self.cache[args]
#       else:
#          value = self.func(*args)
#          self.cache[args] = value
#          return value
#    def __repr__(self):
#       '''Return the function's docstring.'''
#       return self.func.__doc__
#    def __get__(self, obj, objtype):
#       '''Support instance methods.'''
#       return functools.partial(self.__call__, obj)



def getMax(heights): #returns indices of the maximum values in an array heights
    tallest_list = []
    for i in xrange(0,len(heights)):
        if heights[i] == max(heights):
            tallest_list.append(i)
    return tallest_list


def toTheLeftCalc(heights,array): #array is a list of [index for which toTheLeft starts from, count thus far]
    index = array[0]
    if index == 0 or index == 1:
        if array[1] == -1:
            array[1] = 0
        return array
    else:
        count = array[1]
        localLeftMaxIndex = next(k for k in xrange(0,index-1) if heights[k] == max(heights[0:index-1])) #gives the index of the local leftward maximum
        if localLeftMaxIndex == index-1:
            array[0] = localLeftMaxIndex
            array[1] = count
            if array[1] == -1:
                array[1] = 0
            return array
        else:        
            for i in xrange(localLeftMaxIndex,index):
                count+=(max(heights[0:index-1]) - heights[i])
            array[0] = localLeftMaxIndex
            array[1] = count
            if array[1] == -1:
                array[1] = 0            
            return array

def toTheRightCalc(heights,array): #array is a list of [index for which toTheLeft starts from, count thus far]
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

            for m in range(index+1,len(heights)):
                count+=(a-heights[m])
            array[0] = localRightMaxIndex
            array[1] = count    
            return array


def answer(heights):
    b = getMax(heights) #list of all maximums
    c = b[len(b)-1] #index of rightmost maximum
    array = [c,0] #this is what we plug into toTheLeft and toTheRight - the starting index plus the beginning count.
    x = 0
    while x<9000 and array[0]>0:
        array = toTheLeftCalc(heights,array)
        x+=1
    else:
        array[0] = c
        while x<18000 and array[0]<len(heights)-1:
            array = toTheRightCalc(heights,array)
            x+=1
        return array[1]

heights = [1, 4, 2, 5, 1, 2, 3]

print answer(heights)

