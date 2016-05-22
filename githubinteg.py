
def main(request):
    _roundNumber(4.12345, 2)



def _normaliseDegree(targetArray, numOfNodes):
    if numOfNodes == 0:
        return 0

    index = 0
    #To normalize the degree, degree is divided by n-1, where n is the number of vertices in the graph.
    for num in targetArray:
        targetArray[index] = float(num) / (numOfNodes - 1)
        index = index + 1

    return targetArray

def _roundNumbers(targetArray, digits):
    index = 0
    for num in targetArray:
        targetArray[index] = _roundNumber(num, digits)
        index = index + 1

    return targetArray

def _roundNumber(target, digits):
    return round(target, digits)

