# function to find the maximum range of time intervals

def findMaxRange(intervalsArray, n):
    # sort given set of intervals
    sortedArr = sorted(intervalsArray,key=lambda x: x[1])
    minValue = 10000000
    total = 0
    index = 0

    # get the min range that when removed will give max value
    for i in range(n):
        var1 = sortedArr[i][0] if (i < n-1) else 10000000
        var2 = sortedArr[i][1] if (i>0) else -1
        impact = min(sortedArr[i][1], var1) - max(sortedArr[i][0], var2)
        if impact < minValue :
            minValue = impact
    
    # get max contiguous intervals 
    for i in range(n):
        if sortedArr[index][1] >= sortedArr[i][1]:
            sortedArr[index][1] = max(sortedArr[index][1], sortedArr[i][1])
            sortedArr[index][0] = min(sortedArr[index][0], sortedArr[i][0])
        else:
            index+=1
            sortedArr[index] = sortedArr[i]  
    # Total range of maximum contiguous intervals
    for i in range(index):
        total = total + sortedArr[i][1] - sortedArr[i][0]
    
    # Return the difference of total range and minimum impact value
    minValue = 0 if minValue < 0 else minValue
    return (total - minValue)
    
# function for I/O
def readInput():
    for i in range(1,11):
        fileName = 'input/' + str(i) + '.in'
        with open(fileName) as f:
           numberOfRows = [int(x) for x in next(f).split()][0]
           intervalsArray = [[int(x) for x in line.split()] for line in f]
           max = findMaxRange(intervalsArray, numberOfRows)
           newFileName = 'output/' + str(i) + '.out'
           file = open(newFileName, 'w')
           file.write(str(max))

readInput()        