"""
As more and more rabbits were rescued from Professor Booleans horrid laboratory, you had to develop a system to track them, since some habitually continue to gnaw on the heads of their brethren and need extra supervision. For obvious reasons, you based your rabbit survivor tracking system on a binary search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days) and each, luckily enough, had a distinct age. For a given group, the first rabbit became the root, and then the next one (taken in order of rescue) was added, older ages to the left and younger to the right. The order that the rabbits returned to you determined the end pattern of the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation, and you need to make sure that all of the modifications or pathogens introduced by Professor Boolean are contained properly. Since the tree did not preserve the order of rescue, it falls to you to figure out how many different sequences of rabbits could have produced an identical tree to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it would result in a binary tree identical to one created from [5, 2, 9, 1, 8]. 

You must write a function answer(seq) that takes an array of up to 50 integers and returns a string representing the number (in base-10) of sequences that would result in the same tree as the given sequence.


Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"

====


seq = [5,9,8,10,2,1,3,0] gives us this. The binary tree tries to fill up empty nodes first.

                  5
            2           9
        1      3     8     10
    0

We define each subtree as a number (choose whichever) plus all the nodes connected to it. So in this case 0 is technically a subtree with nothing to its right or left,
1 is the root of a subtree with only a leftward root, 2 is the root of a subtree with nodes 1,3,0.

This means that each subtree recursively contains a bunch more subtrees until the base case, which is when a subtree only has a root (has no more nodes below it).



"""


# class Token(object):
#     def __init__(self,value,depth,root):
#         self.root = root
#         self.value = value # token value
#         self.depth = depth # 1 is just underneath the root, larger numbers mean they're further down
#         self.subtree = "R" if self.value > root else "L" #True or False
#     def __str__(self):
#         return "Value={} Depth={} Subtree={}".format(self.value,self.depth,self.subtree)


def subtree_split(lst):
    root = lst[0]
    smallLst = [c for c in lst if c < root]
    largeLst = [c for c in lst if c > root]
    return root,smallLst,largeLst


def count_possibilities1(index, tree, LTree, RTree, combinations, exclude, cache): #initialize this with the index of the tree we want, plus both trees and an exclude clause
    if len(LTree)>0 and len(RTree)>0:
        if tree is LTree:
            this = LTree #if we start at the last index, it should be a leaf on the tree
            that = RTree
        elif tree is RTree:
            this = RTree
            that = LTree
            # if this[index]
        if index == 0:
            combinations+=1
            cache[this[index]]=combinations#1
            return combinations#1 #combinations#+1
        try:
            return cache[this[index]]
        except:
            exclude.add(this[index])
            thatStart = next((i for i in range(len(that)-1,-1,-1) if that[i] not in exclude),0)
            # print thatStart
            combinations = count_possibilities1(index-1,this,LTree,RTree,combinations,exclude,cache)
            # combinations +=1
            combinations = count_possibilities1(thatStart,that,LTree,RTree,combinations,exclude,cache)
            cache[this[index]] = combinations
            # print cache
            return combinations
    else:
        # print LTree,RTree
        return 0

from math import factorial 
def nChooseK(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))
# print nChooseK(7,2)

def answer(seq):
    # Lexclude = set()
    # Lcache = {}
    a,b,c = subtree_split(seq)
    # LCount=0
    # RCount=0
    # if len(b)>0:
    #     LCount = count_possibilities1(len(b)-1,b,b,c,0,Lexclude,Lcache)
    # else:
    #     LCount=1
    # print LCount
    # Rcache = {}
    # Rexclude = set()
    # if len(c)>0:
    #     RCount = count_possibilities1(len(c)-1,c,b,c,0,Rexclude,Rcache)
    # print RCount
    n = len(b)
    m = len(c)
    return str(nChooseK((n+m),n))
    # return LCount+RCount

print answer([5,9,8,2,1,3])

# def count_possibilities2(tree1,tree2,exclude,cache):#each tree is a list of numbers 
#     i = 1
#     j = 1


# def count_possibilities(token, LTree, RTree, exclude):
#     conj = {"L":RTree,"R":LTree}
#     if token.depth == 1:
#         if [t for t in conj[token.subtree] if t.depth==1 and t not in exclude]:
#             return 1
#         else:
#             return 0
#     else:
#         return count_possibilities
#     return conj

# e = Token(0,0,0)

# print count_possibilities(e,b,c,None)

    

