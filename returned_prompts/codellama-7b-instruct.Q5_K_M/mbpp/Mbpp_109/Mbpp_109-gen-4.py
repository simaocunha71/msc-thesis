"""
def odd_Equivalent(binaryString, numberOfRotations):
    # Write your code here
    newString = ""
    for i in range(numberOfRotations):
        newString = binaryString[-1] + binaryString[:-1]
    count = 0
    for i in newString:
        if int(i) % 2 != 0:
            count += 1
    return count
"""