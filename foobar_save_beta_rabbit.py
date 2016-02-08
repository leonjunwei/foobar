import collections
import functools


from random import randint

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

grid = []
for i in range(5):
  gridrow = []
  for j in range(5):
    gridrow.append(randint(0,21))
  grid.append(gridrow)
print grid

def answer(total, grid):
    
    #Brute force would take 10^11 steps for a 20x20 grid so I looked online - sorry!

    @memoized
    def r(t, i, j):
        t -= grid[i][j] #this bit is important! subtract the number on the square from the total.
        if i < 0 or j < 0 or t < 0:
            print "we're done here. ", total + 1
            return total + 1
        elif i == j == 0:
            print "reached beginning: ", t
            return t
        else:
            print "recursion: ", min(r(t, i - 1, j), r(t, i, j - 1))
            return min(r(t, i - 1, j), r(t, i, j - 1)) #

    remainder = r(total, len(grid) - 1, len(grid) - 1)
    print "remainder is: ", remainder

    if remainder <= total:
        print "returning results: ", remainder
        return remainder  
    else:
        return -1
print answer(115, grid)