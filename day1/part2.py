from input import input

listSum = [sum(val) for val in input]
listSum.sort(reverse = True)
print(listSum[0] + listSum[1] + listSum[2])