    def search(lst):
        from collections import Counter
        counter = Counter(lst)
        for num in sorted(counter.keys(), reverse=True):
            if num > 0 and num <= counter[num]:
                return num
        return -1


# Test cases
print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1
print(search([10, 10, 10, 9, 9]))  # Output: 10
print(search([1, 1, 1, 1]))  # Output: 1
print(search([1]))  # Output: 1
print(search([2, 2, 2, 3, 3]))  # Output: 2
print(search([1, 2, 2, 2, 3, 4, 4, 5]))  # Output: 2
print(search([1, 1, 1, 1, 1, 1, 1]))  # Output: 1
print(search([2, 2, 2, 2, 2, 2]))  # Output: 2
print(search([3, 3, 3, 3, 3, 3]))  # Output: 3
print(search([4, 4, 4, 4, 4, 4]))  # Output: 4
print(search([5, 5, 5, 5, 5, 5]))  # Output: 5
print(search([6, 6, 6, 6, 6, 6]))  # Output: 6
print(search([7, 7, 7, 7, 7, 7]))  # Output: 7
print(search([8, 8, 8, 8, 8, 8]))  # Output: 8
print(search([9, 9, 9, 9, 9, 9]))  # Output: 9
print(search([10, 10, 10, 