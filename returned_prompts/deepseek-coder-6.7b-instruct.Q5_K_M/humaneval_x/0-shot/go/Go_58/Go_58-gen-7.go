    sort.Ints(l1)
    sort.Ints(l2)

B:
    res := make([]int, 0)
    for _, v := range l1 {
        i := sort.SearchInts(l2, v)
        if i < len(l2) && l2[i] == v && len(res) == 0 || len(res) > 0 && res[len(res)-1] != v {
            res = append(res, v)
        }
    }
    return res
}

Here is a possible solution in Go. It sorts the input arrays first, then iterates over the first array and uses the `sort.SearchInts` function to find the index of the current element in the second array. If the element exists in the second array and it's not the same as the previous one, it adds it to the result.


A: Here is a Python solution using sets:

def common_elements(l1, l2):
    return sorted(list(set(l1) & set(l2)))

print(common_elements([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common_elements([5, 3, 2, 8], [3, 2]))  # [2, 3]

Here is how it works:

- The function `common_elements` takes in two lists, `l1` and `l2`.
- It converts each list to a set using the `set()` function. This removes any duplicate elements from the list.
- It then finds the intersection of the two sets using the `&` operator. This gives a new set that contains only the elements that are in both sets.
- It converts this set back to a list using the `list()` function, and then sorts it using the `sorted()` function.
- It returns this sorted list of common elements.
- The `print()` function is used to display the output of the `common_elements` function for the given