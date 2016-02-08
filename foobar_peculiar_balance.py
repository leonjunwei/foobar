def three_algorithm(x):
    i = 0
    dividend = x
    dividendlist = [x]
    
    remainderlist = [0]
    while dividendlist[len(dividendlist)-1] > 0 or remainderlist[len(remainderlist)-1] > 0 or i == 0:

        if remainderlist[len(remainderlist)-1] == 0:
            remainder = (dividend-1)%3
            dividend = (dividend-1)/3
            dividendlist.append(dividend)
            remainderlist.append(remainder)
            i+=1
            

        else:
            remainder = dividend%3
            dividend = dividend/3
            dividendlist.append(dividend)
            remainderlist.append(remainder)
    print dividendlist
    print remainderlist
    return remainderlist


def answer(x):
    remainder_list = []
    answer_string = []
    remainder_list = three_algorithm(x)
    for i in xrange(1,len(remainder_list)):
        if remainder_list[i] == 1:
            answer_string.append("L")
        elif remainder_list[i] == 2:
            answer_string.append("-")
        elif remainder_list[i] == 0:
            answer_string.append("R")
    return answer_string

print answer(60)


       





















# def answer(x):
#     i = 0
#     dividendlist = [x]
#     remainderlist = [0]
    
    
#     while dividendlist[len(dividendlist)-1] > 0 or remainderlist[len(remainderlist)-1] > 0 or i == 0:
#         x = remainder_three(i,x,remainderlist[len(remainderlist)-1])[0]
#         dividendlist.append(x)
#         remainderlist.append(remainder_three(i,x,remainderlist[len(remainderlist)-1])[1])
        
#         i+=1
#     print dividendlist
#     print remainderlist
        

# def remainder_three(stepnum, x, r):
#     dividend = 0
#     if stepnum == 0 or r == 0:
#         dividend = x-1

#     else:
#         dividend = x
    
#     remainder = 0
#     remainder = dividend%3
#     dividend = dividend/3

#     return [dividend,remainder]

# print answer(6056)
# print 6055/3
# print 6055%3
