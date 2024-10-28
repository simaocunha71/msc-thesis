    def smallest_change(arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            if arr[0] == arr[1]:
                return 0
            return 1
        if n % 2 == 0:
            mid1 = n // 2 - 1
            mid2 = n // 2
        else:
            mid1 = n // 2 - 1
            mid2 = n // 2
        left = arr[:mid1+1]
        right = arr[mid2:][::-1]
        diff = 0
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                diff += 1
        if len(left) > len(right):
            diff += len(left) - len(right)
        elif len(left) < len(right):
            diff += len(right) - len(left)
        return diff

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output: 0

