def last(a,x):
    n = len(a)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
        else:
            if mid == n - 1 or a[mid + 1] < x:
                return mid
            else:
                right = mid - 1
    return left

def main():
    a = [1,2,3]
    assert last(a,1) == 0
    print("All Tests Passed")

if __name__ == "__main__":
    main()



"""
Test Cases:
assert last([1,2,3],1) == 0
assert last([1,2,3],2) == 1
assert last([1,2,3],3) == 2
assert last([1,2,3],4) == 3
"""




















"""
def last(a,x):
    n = len(a)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
        else:
            if mid == n - 1 or a[mid + 1] < x:
                return mid
            else:
                right = mid - 1
    return left

def main():
    a = [1,2,3]
    assert last(a,1) == 0
    print("All Tests Passed")

if __name__ == "__main__":
    main()
"""

"""
def last(a,x):
    n = len(a)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 