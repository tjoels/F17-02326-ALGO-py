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
Generates an array populated with random integers
'''
from random import sample

def randomintarray(listamount):
    list = sample(range(listamount), k=listamount) # create list of increasing size with random integers in range(size)
    print(list)
    return list

'''
Calls randomintarray to generate list
and sorts it by calling insertionsort
returns sorted list
'''
import time
#millis = int(round(time.time() * 1000))
#print millis
def randomsorter(listamount):
    currentList = randomintarray(listamount)
    #sortedList = []

    startmillis = int(round(time.time() * 1000))
    sortedList = insertionsort(currentList)
    endmillis = int(round(time.time() * 1000))
    timetaken = endmillis-startmillis
    print(sortedList)
    print("Sortingtime in ms", listamount, "elements:", timetaken)
    return sortedList

randomsorter(15000)
