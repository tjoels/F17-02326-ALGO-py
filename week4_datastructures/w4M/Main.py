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

def randomintarray(startingnumber, listAmount):
    aList = [] # create aList object of type list
    for size in range(startingnumber, listAmount + 1, 5000):
        list = sample(range(size), k=size) # create list of increasing size with random integers in range(size)
        print(list)
        aList.append(list) # append list to aList
    #print(aList)
    return aList

'''
Calls randomintarray to generate lists,
and sorts them by calling insertionsort upon each list
returns list of sorted lists
'''
import time
#millis = int(round(time.time() * 1000))
#print millis
def randomsorter(startingnumber, listAmount):
    currentList = randomintarray(startingnumber, listAmount)
    sortedList = []
    for i in range(0, listAmount-startingnumber+1): # Loops through generated lists (diff of interval plus 1)
        startmillis = int(round(time.time() * 1000))
        sortedList.append(insertionsort(currentList[i]))
        endmillis = int(round(time.time() * 1000))
        timetaken = endmillis-startmillis
        print("Sortingtime", (i*5000)+startingnumber, "elements:", timetaken)
    print(sortedList)
    return sortedList

randomsorter(0, 20000)
