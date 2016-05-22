
def main(request):
    _roundNumber(4.12345, 2)
    

def _roundNumbers(targetArray, digits):
    index = 0
    for num in targetArray:
        targetArray[index] = _roundNumber(num, digits)
        index = index + 1

    return targetArray
    
def _roundNumber(target, digits):
    return round(target, digits)

