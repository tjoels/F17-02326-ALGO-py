class RandomIntArray:
    '''
    Generates arrays of increasing sizes populated with random integers
    '''
    from random import sample

    def randomintarray(listAmount):
        aList = [] # create aList object of type list
        for size in range(1, listAmount + 1):
            list = sample(range(1000), k=size) # create list of increasing size with random integers
            print(list)
            aList.append(list) # append list to aList
        return aList
