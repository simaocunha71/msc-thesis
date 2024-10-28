    # O(n) solution
    def smallest_change(arr):
        count = 0
        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr)-1-i]:
                count += 1
        return count

    return smallest_change(arr)



# Running Tests
test_arr = [1, 2, 3, 5, 4, 7, 9, 6]
test_arr_2 = [1, 2, 3, 4, 3, 2, 2]
test_arr_3 = [1, 2, 3, 2, 1]

# print(smallest_change(test_arr)) # 4
# print(smallest_change(test_arr_2)) # 1
# print(smallest_change(test_arr_3)) # 0


# Time Complexity: O(n)
# Space Complexity: O(1)

```
