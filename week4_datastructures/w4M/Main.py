"""
Implemented with the aid of
CLRS Chapter 2 insertion sort pseudo code.
A is an array that is to get sorted.
"""
def insertionsort(A):
    for j in range(1, len(A)):
        key = A[j]
        # position = A[j - 1]
        # Insert  A[j] into sorted sequence A[1 .. j - 1].
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

'''
Generates arrays of increasing sizes populated with random integers
'''
from random import sample

def randomintarray(listAmount):
    aList = [] # create aList object of type list
    for size in range(1, listAmount + 1):
        list = sample(range(size), k=size) # create list of increasing size with random integers in range(size)
        #print(list)
        aList.append(list) # append list to aList
    #print(aList)
    return aList

'''
Calls randomintarray to generate lists,
and sorts them by calling insertionsort upon each list
returns list of sorted lists
'''
def randomsorter(listAmount):
    currentList = randomintarray(listAmount)
    sortedList = []
    for i in range(0, listAmount):
        #print('I' + currentList[i])
        sortedList.append(insertionsort(currentList[i]))
        #print('O' + sortedList)
    print(sortedList)
    return sortedList

randomsorter(10)
