
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    if len(arr) < 2:
        return 0
    else :
        min_val = arr[-1]
        change = abs(min_val - arr[0])
        if not isPalindrome(arr):
            change += smallest_change(arr[1:])

        if not isPalindrome(arr) and change < 2 :
            return 0
        
    # If the array already a palindrome, return as soon as possible.
    if isPalindrome(arr):
        return min_change = 0

def main():
    print("Enter the sequence of numbers:")
    for i in range(1,11):
        arr[i] = input()
    mc=smallest_change(arr)
    print('Minimum change to make this array a palindrome is ',mc,' steps.')
    
main()