#Homework 1 for Algorithms EECS 660

# Banana
# Banana

## Basic names for the open_file
##########################################
##########################################


file_name = "input.txt" #File name
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
    print(pref_xy)
    print(pref_xx)
    return


############################################
############################################




open_file = open(file_name, "r")
pool_size = [int(x) for x in next(open_file).split()]
for line in open_file:
    if line.strip():
        array.append([int(x) for x in line.split()])

man_preference, women_preference = banana_split(array)

stable_matching(pool_size, pool_size, man_preference , women_preference)
