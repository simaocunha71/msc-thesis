
def smallest_change(arr):
    # Write your code here.
    # O(n) time | O(n) space
    # where n is the length of the input array
    # arr: List[int]
    # rtype: int

    # Step 1: Create a list of pairs, each of which is a pair of a number and its count
    # pairs = [[1,2],[3,4],[5,6]]
    # [1,2] means 1 is paired with 2
    # [3,4] means 3 is paired with 4
    # [5,6] means 5 is paired with 6
    pairs = [[arr[i], arr.count(arr[i])] for i in range(len(arr))]

    # Step 2: Sort the pairs by the count of each element
    # pairs = [[5,6],[1,2],[3,4]]
    # [5,6] means 5 is paired with 6
    # [1,2] means 1 is paired with 2
    # [3,4] means 3 is paired with 4
    pairs.sort(key=lambda x: x[1], reverse=True)

    # Step 3: Add up the number of elements that can be paired
    # pairs = [[5,6],[1,2],[3,4]]
    # 5 can be paired with 6, 1 can be paired with 2, 3 can be paired with 4, so we add up to 5 + 2 + 4 = 11
    count = 0
    for pair in pairs:
        count += pair[1]

    # Step 4: Return the number of elements that can be paired
    return count

# Test case 1:
arr = [1,2,3,5,4,7,9,6]
print(smallest_change(arr)) # 4

# Test case 2:
arr = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr)) # 1

# Test case 3:
arr =