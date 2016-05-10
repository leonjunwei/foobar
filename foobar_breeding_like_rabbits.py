
import collections
import functools

"""
Given
R(0)    = 1
R(1)    = 1
R(2)    = 2
R(2t+1) = R(t-1) + R(t)   + 1 for t >= 1
R(2t)   = R(t)   + R(t+1) + t for t > 1,

Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n such that R(n)
= S. Return the answer as a string in base-10 representation.

There might be an algorithm to break S down into R(n), but I decided to take advantage of the fact that R(n) is strictly increasing
above n = 3, as long as you consider the odd cases of n and the even cases of n separately. 

If n > m and (n and m are both odd), R(n) is bigger than R(m)
If n > m and (n and m are both even), R(n) is bigger than R(m)

The even series of R grows more quickly than the odd series. We want to find the last occurence of S, so we check for R(odd) first.

S can be as big as 10**25, which is pretty huge. As such, we use a bisect search to massively cut down on computation time.

"""


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

@memoized #without memoization this'll run incredibly slowly.
def R(n):
    try:
        return {0:1,1:1,2:2,3:3,4:7}[n] #i calculated R(3) and R(4) by hand and put them in, all we need is R(0-2) though 
    except KeyError:
        if n%2==0: #if n = 2t, formula is R(t) + R(t+1) + t
            return R(n/2) + R(n/2+1) + n/2
        else: #if n = 2t+1, formula is R(t-1) + R(t) + 1
            return R((n-1)/2 - 1) + R((n-1)/2) + 1


"""
As mentioned earlier, first we try looking only at odd numbers: if S is R(odd number), that's the last occurence.
Elif S isn't any R(odd number), we then check if S is R(even). If so, that's the last occurence.
Else return "None"

"""

def answerOdd(S): #we try a bisect search, doubling n and converting it into an odd number each time.
    lowB = 1 #initial lower bound for search
    uppB = 3 #initial upper bound for search
    while R(uppB)<S: #increasing n until S falls somewhere between lowB and uppB
        lowB = uppB #as long as uppB is odd, lowB is odd
        uppB = uppB*2 - 1 #uppB is always odd!
    if R(uppB)==S:
        return str(uppB)
    else: #we know R(uppB) is greater than S, but R(lowB) is lower than S.
        mid = (lowB+uppB)/2
        """For the line above I tried using math.ceil, but Python didn't like large numbers and sometimes gave
        me an even number. Since lowB and uppB are always an even number apart, we can just use integer division.
        """
        while uppB-lowB >=2:
            mid = (lowB+uppB)/2
            """Edit: checking if lowB == mid or uppB == mid should be unnecessary."""
            # if lowB == mid or uppB == mid:
                # return None
            if R(mid)>S: #we adjust upper and lower bounds accordingly
                uppB = mid
                mid = (lowB+uppB)/2
            if R(mid)<S:
                lowB = mid
                mid = (lowB+uppB)/2
            if R(mid) == S:
                return mid

def answerEven(S): #we try a bisect search, doubling n each time.
    lowB = 0
    uppB = 2
    while R(uppB)<S: #increasing n until S falls somewhere between lowB and uppB
        lowB = uppB
        uppB = uppB*2 #uppB is always even
    if R(uppB)==S:
        return str(uppB)
    else: #we know R(uppB) is greater than S, but R(lowB) is lower than S.
        mid = (lowB+uppB)/2
        while uppB-lowB >=2:
            mid = (lowB+uppB)/2
            """Edit: checking if lowB == mid or uppB == mid should be unnecessary."""
            # if lowB == mid or uppB == mid:
                # return None
            if R(mid)>S:
                uppB = mid
            if R(mid)<S:
                lowB = mid
            if R(mid) == S:
                return mid

def answer(str_S):
    S = int(str_S)
    if answerOdd(S):
        return str(answerOdd(S))
    elif answerEven(S):
        return str(answerEven(S))
    else:
        return "None"

print R(12837129846)
print answer("120186521781")
print R(2**90-17203)
print answer("28369459233623297966437972604")