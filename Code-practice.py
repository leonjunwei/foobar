



class HashTable(object):
    def __init__(self,size=256,dynamic=True):
        self.size = size
        self.table = [None] * self.size
        self.dynamic = dynamic
        self.numElements = 0
    def __str__(self):
        return str(self.table)
    def hsh(self,key):
        key = str(key)
        total = sum([(3**i)*ord(key[i]) for i in range(len(key))])
        return (total * len(key)) % self.size
    def insert(self, tup): 
    #tup is a (key,value) tuple. Storing stuff in buckets to manage collision.
        key = tup[0]
        value = tup[1]
        index = self.hsh(key)
        if self.retrieve(key) == None: #if the key has never been used before
            if self.table[index] == None:
                self.table[index] = [tup]
                self.numElements +=1
            else: #if the key has never been used before, but there's a hash collision
                self.table[index].append(tup)
                self.numElements +=1
        else: #if the key already has a corresponding value in the hashtable
            self.deleteKey(key)
            self.insert(tup)
        if self.dynamic:
            self.checkForResize()
    def retrieve(self,key,alternative = None):
        index = self.hsh(key)
        # print index
        if self.table[index] == None:
            return alternative
        else:
            for tup in self.table[index]:
                # print tup
                if tup[0] == key:
                    return tup[1]
            return alternative
    def deleteKey(self,key):
        if self.retrieve(key)==None:
            raise KeyError("key " + str(key) + " does not exist")
        else:
            index = self.hsh(key)
            for tup in self.table[index]:
                if tup[0] == key:
                    self.table[index].remove(tup)
    def countSelf(self):
        count = 0
        for bucket in self.table:
            try:
                count += len(bucket)
            except TypeError:
                pass
        return count
    def keyValuePairs(self):
        result = []
        for bucket in self.table:
            try:
                for tup in bucket:
                    result.append(tup)
            except TypeError:
                pass
        return result
    def checkForResize(self):
        if self.numElements >= self.size/2:
            # print self.numElements, self.size
            # print "doubling!"
            tempStore = self.keyValuePairs()
            self.size *= 2
            self.table = [None] * self.size
            self.numElements = 0
            for tup in tempStore:           
                self.insert(tup)
           
# b = HashTable(10, dynamic = True)

# for i in range(30):
#     b.insert((i,i**2))
# store = []
# for i in range(30):
#     store.append(b.retrieve(i))

# print b.table
# print len(b.table)
# print b.retrieve("b")


### Sorting ###

def merge_sort(lst):
  """
  Merge sort is stable, so the order of equal elements in the original list is produced.
  It needs memory on O(n) and tends to not be as fast as quicksort, though
  """
  if len(lst)==1:
      return lst
  elif len(lst)==2: 
      if lst[0] <= lst[1]:
          return lst
      else:
          return lst[::-1]
  else:
      result = []
      i,j = (0,0)
      left = merge_sort(lst[:len(lst)/2])
      right = merge_sort(lst[len(lst)/2:])
      while len(result)<len(left)+len(right):
          if i==len(left):
              result.extend(right[j:])
          elif j==len(right):
              result.extend(left[i:])
          elif i<=len(left)-1 and left[i]<=right[j]:
              result.append(left[i])
              i+=1
          elif j<=len(right)-1 and left[i]>right[j]:
              result.append(right[j])
              j+=1
      return result

# print merge_sort([1,7,5,3,11,19,2,8,4,6])



def quick_sort(lst): 
  """
  Quicksort is faster than mergesort but is unstable.
  This implementation might actually be pretty crappy.
  """
  if len(lst) < 2:
      return lst
  else: # O(log n) on average, since we need to break lst down into individual components 
      pivot = lst[len(lst)/2] #O(1)

      left = []
      middle = []
      right = []
      for a in lst:
          if a<pivot:
              left.append(a)
          elif a>pivot:
              right.append(a)
          else:
              middle.append(a)
      return quick_sort(left)+middle+quick_sort(right)

      #return quick_sort([k for k in lst if k<pivot]) + [k for k in lst if k==pivot] + quick_sort([k for k in lst if k>pivot]) 
          #this oneliner is O(3n), but we could make it O(1.5n) on average by iterating through the list and comparing each element with pivot

# a = [1,7,5,3,11,19,2,8,4,6,2,2,2,2,2,22,1]
# print len(a)==len(quick_sort(a))
# print quick_sort(a)



### Equilibrium index ###

def find_equilibrium(A):
    # write your code in Python 2.7  
    #An empty array has no equilibrium index because it doesn't have an index, I think
    for index in range(len(A)):
        if index == 0:
            leftSum = 0
            rightSum = sum(A[1:])
        else:
            leftSum+=A[index-1] #at index 1, the left sum is A[0], or 0+A[0]
            rightSum-=A[index]  #the right sum is now A[2:], or A[1:]-A[1]
            """ At index n, the left sum is A[0]+A[1]+...+A[n-1]
                The right sum is A[n+1]+...+A[N-1]
                At the last index A[N-1], the left sum will evaluate to A[0]+...+A[N-2] and the right sum will evaluate to 0.

            """
        if leftSum == rightSum:
            return index
    return -1
        


# lst = [-1,3,-4,5,1,-6,2,1]
# lst2 = [1,1,1,1,1,1,1,1,1,1,0,10]

# print find_equilibrium([])