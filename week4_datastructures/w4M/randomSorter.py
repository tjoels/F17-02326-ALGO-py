from w4M import InsertionSort, RandomIntArray

class RandomSorter:

    def randomsorter(listAmount):
        currentList = RandomIntArray(listAmount)) # TODO: is not callable
        for i in range(0, listAmount):
            print('I' + currentList[i])
            sortedList = insertionSort(currentList[i])
            print('O' + sortedList)
        return sortedList

# RandomSorter.randomsorter(2)