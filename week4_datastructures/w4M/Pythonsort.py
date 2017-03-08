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
and sorts it with Python's built in sort() method.
returns sorted list
'''
import time
#millis = int(round(time.time() * 1000))
#print millis
def randomsorter(listamount):
    currentList = randomintarray(listamount)
    #sortedList = []

    startmillis = int(round(time.time() * 1000))
    currentList.sort()
    endmillis = int(round(time.time() * 1000))
    timetaken = endmillis-startmillis
    print(currentList)
    print("Sortingtime in ms", listamount, "elements:", timetaken)
    return currentList

randomsorter(15000)
