"""
def search(array):
    for i in range(0,len(array)-1):
        if array[i]!=array[i+1]:
            return array[i+1]
    return array[-1]
"""

def search(array):
    for i in range(0,len(array)-1):
        if array[i]!=array[i+1]:
            return array[i+1]
    return array[-1]


# assert search([1,1,2,2,3]) == 3
# assert search([1,2,3,4,4,4,5,5]) == 5
# assert search([1,2,3,4,4,4,4,5]) == 3
# assert search([1,2,3,4,4,4,4,5,5,5]) == 3
# assert search([1,1,2,2,3,3,3,4]) == 4


# assert search([1,1,2,2,3]) == 3
# assert search([1,2,3,4,4,4,5,5]) == 5
# assert search([1,2,3,4,4,4,4,5]) == 3
# assert search([1,2,3,4,4,4,4,5,5,5]) == 3
# assert search([1,1,2,2,3,3,3,4]) == 4

# assert search([1,1,2,2,3]) == 3
# assert search([1,2,3,4,4,4,5,5]) == 5
# assert search([1,2,3,4,4,4,4,5]) == 3
# assert search([1,2,3,4,4,4,4,5,5,5]) == 3
# assert search([1,1,2,2,3,3,3,4]) == 4

# assert search([1,1,2,2,3]) == 3
# assert search([1,2,3,4,4,4,5,5]) == 5
# assert search