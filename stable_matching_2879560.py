#Homework 1 for Algorithms EECS 660
import sys
# Banana
# Banana

## Basic names for the open_file
##########################################
##########################################


file_name = sys.argv[1] #File name
pool_size =0; #Size of the number of individuals
array = [] # array containing all input
man_preference = []
women_preference = []


##########################################
##########################################
# Functions
##########################################
##########################################

def banana_split(not_split):
    half = len(not_split) //2
    return not_split[:half], not_split[half:]

def stable_matching(xy,xx, pref_xy , pref_xx):


    list_of_men = []

    for i in range(xy+1):
        list_of_men.append(i) # Contains a list of the men who haven't gone yet.

    list_of_men.remove(0)

    taken_women = [None] * (xy)
    taken_by = [None] * (xy)

    try_count = [0] *(xy)

    #print(list_of_men)
    while len(list_of_men) != 0:
        proposal_list = pref_xy[list_of_men[0]-1]
        current_proposal = proposal_list[try_count[list_of_men[0]-1]]
        try_count[list_of_men[0]-1] = try_count[list_of_men[0]-1]+1
        if taken_women[current_proposal-1] == None:
            taken_by[current_proposal-1]= list_of_men[0]
            taken_women[current_proposal-1] = "Yes"
            list_of_men.pop(0)
        else:
            man_who_holds_women = taken_by[current_proposal-1]
            wproposal_list = pref_xx[current_proposal-1]
            index_one = wproposal_list.index(man_who_holds_women)
            index_two = wproposal_list.index(list_of_men[0])

            if index_one > index_two:
                taken_women[current_proposal-1] = "Yes"
                taken_by[current_proposal-1] = list_of_men[0]
                list_of_men[0] = man_who_holds_women

    final_list = []
    for i in taken_by:
        a_list = (i, taken_by.index(i)+1)
        final_list.append(a_list)

    final_list.sort(key = lambda x:x[0])
    for i in final_list:
        print (str(i)[1:-1])

    return


############################################
############################################




open_file = open(file_name, "r")
pool_size = [int(x) for x in next(open_file).split()]
for line in open_file:
    if line.strip():
        array.append([int(x) for x in line.split(",")])


man_preference, women_preference = banana_split(array)

stable_matching(pool_size[0], pool_size[0], man_preference , women_preference)
