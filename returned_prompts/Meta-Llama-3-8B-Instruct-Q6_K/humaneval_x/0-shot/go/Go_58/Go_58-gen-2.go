Here is the solution using Go programming language:

```go
package main

import (
    "sort"
)

func Common(l1 []int, l2 []int) []int {
    // Convert slices to sets
    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    for _, v := range l1 {
        set1[v] = true
    }
    for _, v := range l2 {
        set2[v] = true
    }

    // Find common elements
    common := make([]int, 0)
    for k := range set1 {
        if set2[k] {
            common = append(common, k)
        }
    }

    // Sort the common elements
    sort.Ints(common)

    return common
}

func main() {
    l1 := []int{1, 4, 3, 34, 653, 2, 5}
    l2 := []int{5, 7, 1, 5, 9, 653, 121}
    result := Common(l1, l2)
    print(result) // Output: [1 5 653]

    l3 := []int{5, 3, 2, 8}
    l4 := []int{3, 2}
    result = Common(l3, l4)
    print(result) // Output: [2 3]
}
```

The solution works by first converting the input lists to sets (maps in Go), then finding the common elements by iterating over the sets, and finally sorting the common elements. This solution assumes that the input lists do not contain duplicate elements, as per the problem statement. If the input lists may contain duplicates, the solution should be modified to handle this case. 

This solution has a time complexity of O(n + m), where n and m are the lengths of the input lists, as it iterates over the lists to convert them to sets and then finds the common elements. The space complexity is also O(n + m), as it creates sets to store the elements of the input lists. 

The `sort.Ints` function is used to sort the common elements. This function has a time complexity of O(n log n), where n is the length of the slice being sorted, and a space complexity of O(n), as it creates a new slice to store the sorted elements. 

In the `main` function, the `Common` function is called with different