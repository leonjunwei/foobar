population = [[6, 7, 2, 7, 6], [6, 3, 1, 10000, 7]]
# # print len(population) #len(population) is 2, i.e. len(population) is the height of the list

# # print len(population[0]) is 5, i.e. len(population[0]) is the width of the list
    
# for i in population:
#     print i

# print population[1][3] # [1][3] means second row, 4th column


# iterating over the entire grid is like:

def i_check(pop,array,strength):
    y=0
    x=0
    y = array[0]
    x = array[1]
    if pop[y][x] == -1:
        for i in xrange(-1,2,1): #for each row
            if y+i <= len(pop)-1 and y+i >=0 and strength >= pop[y+i][x]:
                pop[y+i][x] = -1
            for j in xrange(-1,2,1): #each column in each row 
                if x+j >= 0 and x+j <= len(pop[0])-1 and strength >= pop[y][x+j]:
                    pop[y][x+j] = -1
    return pop


def answer(population,x,y,strength):
    count = 0

    i_list = []
    population_new = []
    if strength >= population[y][x]:
        population_new = population
        population_new[y][x] = -1
        i_list.append([y,x])
        
        while count <=100:
            population = population_new
            for i in xrange(0,len(population_new)):
                for j in xrange(0,len(population_new[0])):
                    population_new = i_check(population_new,[i,j],strength)
            count+=1
            
           
    return population_new

        
print answer([[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]],2,1,5)


