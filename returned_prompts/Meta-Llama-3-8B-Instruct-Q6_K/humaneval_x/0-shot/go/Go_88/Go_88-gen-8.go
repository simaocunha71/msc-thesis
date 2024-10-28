Here is a Go solution for the problem:

```go
import (
    "sort"
)

func SortArray(array []int) []int {
    if len(array) == 0 {
        return array
    }
    sum := array[0] + array[len(array)-1]
    if sum%2 == 0 {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    } else {
        sort.Ints(array)
    }
    return array
}
```

Explanation:

1. First, we check if the array is empty. If it is, we return it as is.

2. We calculate the sum of the first and last elements of the array.

3. If the sum is even, we sort the array in descending order.

4. If the sum is odd, we sort the array in ascending order.

5. We return the sorted array.

Note: In Go, we use the `sort` package to sort slices. The `sort.Ints` function sorts the slice in ascending order, and the `sort.Reverse` function sorts the slice in descending order. We use the `sort.IntSlice` type to create a slice of integers that we can sort. The `sort.Sort` function sorts the slice in place. We pass the slice to the `sort.Sort` function, and it sorts the slice according to the order specified. The sorted slice is then returned.