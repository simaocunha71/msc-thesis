    var res []int
    // Combine two slices
    combined := append(l1, l2...)
    // Sort the combined slice
    sort.Ints(combined)
    // Remove duplicates
    prev := combined[0]
    res = append(res, prev)
    for i := 1; i < len(combined); i++ {
        if prev != combined[i] {
            res = append(res, combined[i])
            prev = combined[i]
        }
    }
    return res
}




In the above code, we first combine the two slices into one using `append()`, then we sort the combined slice using `sort.Ints()`. After that, we remove the duplicate elements by iterating through the sorted slice and appending the unique elements to the `res` slice.

Note that we don't need to sort the original slices `l1` and `l2` because `append()` guarantees that the order of elements in the combined slice will be the same as the order of elements in the original slices.

The time complexity of this solution is O(n log n), where n is the total number of elements in both slices. This is because we are sorting the combined slice of size n, and then iterating through it to remove duplicates.

The space complexity of this solution is also O(n), as we are creating a new slice `combined` to store all the elements from both slices, and another slice `res` to store the unique elements.

Overall, this solution provides an efficient way to find the common elements of two lists while ensuring uniqueness and sorting the result.





































































































































