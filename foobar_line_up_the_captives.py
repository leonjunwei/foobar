"""
To help plan this caper you need to calculate how many ways the rabbits can be lined up such that a viewer on one end sees x rabbits, 
and a viewer on the other end sees y rabbits, because some taller rabbits block the view of the shorter ones.

For example, if the rabbits were arranged in line with heights 30 cm, 10 cm, 50 cm, 40 cm, and then 20 cm, a guard looking from the left side would see 2 rabbits 
(30 and 50 cm) while a guard looking from the right side would see 3 rabbits (20, 40 and 50 cm). 

Write a method answer(x,y,n) which returns the number of possible ways to arrange n rabbits of unique heights along an east to west line, so that only x are 
visible from the west, and only y are visible from the east. The return value must be a string representing the number in base 10.

If there is no possible arrangement, return "0".

The number of rabbits (n) will be as small as 3 or as large as 40.
The viewable rabbits from either side (x and y) will be as small as 1 and as large as the total number of rabbits (n).

Test cases
==========

Inputs:
    (int) x = 2
    (int) y = 2
    (int) n = 3
Output:
    (string) "2"

Inputs:
    (int) x = 1
    (int) y = 2
    (int) n = 6
Output:
    (string) "24"


This is not a brute-force computational problem - 40! is in the order of 10**47. There's some form of algorithm, maybe.

Take one specific case - x = 1, y = 3. The tallest rabbit has to be on the left, and on the right we can have (second tallest rabbit) hide as many as he wants.
Any 1 rabbits can then appear in front, and hide anywhere from none to all of the rabbits shorter than them. Each of the hidden pockets then has its own permutation.


If we want to see 2 rabbits from each side, we effectively need 2 other peaks besides the tallest dude.

If we want to see 3 from the left and 4 from the right, we need 2 peaks on the left and 3 on the right, and one dude in the center.

That means we need x+y-2 peaks plus the tallest dude.

Maybe if we have the tallest rabbit on the right and x+y-2 peaks when viewed from the left, there will be the same number of permutations. This makes the problem much more straightforward.


"""
import collections
import functools
from math import factorial

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


def answer(x, y, n):
    if x+y>n+1:
        return "0"
    @memoized
    def r(n, x, y):
        t = n-1
        print x, y, n
        if n == 1 and y == 0 and x == 0:
            return 1
        elif n<=x+y:
            return 0
        elif x == 1:
            return factorial(n-1)
        elif y == 1:
            return factorial(n-1)
        elif x<=0 and y<=0:
            return 0
        elif x<=0:
            return (f(n-1,x,y))+r(n-1,x,y-1)
        elif y<=0:
            return (f(n-1,x,y))+r(n-1,x-1,y)
        else:
            print "recursion."
            return (f(n-1,x,y))+r(n-1,x-1,y)+r(n-1,x,y-1)
    @memoized
    def f(n,x,y):
      return (r(n-1,x,y))*(n-1)+r(n-1,x-1,y)+r(n-1,x,y-1)

    return str(int(r(n,x-1,y-1)))

print answer(1,2,6)

