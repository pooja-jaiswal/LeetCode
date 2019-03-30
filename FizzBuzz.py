def fizzBuzz(n):
    tempList = []
    for each in range(1,n+1):
        if each%3 == 0 and each%5 == 0:
            tempList.append("FizzBuzz")
        elif each%5 == 0:
            tempList.append("Buzz")
        elif each%3 == 0:
            tempList.append("Fizz")
        else:
            tempList.append(str(each))
    return tempList