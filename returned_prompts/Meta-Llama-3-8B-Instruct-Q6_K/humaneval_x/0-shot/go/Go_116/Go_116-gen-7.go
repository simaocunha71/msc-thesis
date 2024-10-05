Here is the solution to the problem:

```go
import (
    "fmt"
    "sort"
)

// In this Kata, you have to sort an array of non-negative integers according to
// number of ones in their binary representation in ascending order.
// For similar number of ones, sort based on decimal value.
// 
// It must be implemented like this:
// >>> SortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
// >>> SortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
// >>> SortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]

func SortArray(arr []int) []int {
    type pair struct {
        num  int
        ones int
    }

    sort.Slice(arr, func(i, j int) bool {
        p := pair{num: arr[i], ones: binCount(arr[i])}
        q := pair{num: arr[j], ones: binCount(arr[j])}

        if p.ones != q.ones {
            return p.ones < q.ones
        }
        return p.num < q.num
    })

    return arr
}

func binCount(n int) int {
    count := 0
    for n > 0 {
        n = n & (n - 1)
        count++
    }
    return count
}
```


This function `SortArray` sorts an array of non-negative integers according to the number of ones in their binary representation in ascending order. For similar number of ones, it sorts based on decimal value. The function uses a custom type `pair` to hold the number and the number of ones in the binary representation. The `sort.Slice` function is used to sort the array. The comparison function within `sort.Slice` returns true if the number of ones in the binary representation of the pair at index `i` is less than the number of ones in the binary representation of the pair at index `j`. If the number of ones is the same, it compares the decimal values. The `binCount` function counts the number of ones in the binary representation of a number. It does this by using bitwise operations to remove the least significant 1 bit from the number as long as there is at least