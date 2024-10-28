Here is the solution in Go:

```go
import (
    "fmt"
    "sort"
)

type pair struct {
    val int
    ones int
}

func SortArray(arr []int) []int {
    pairs := make([]pair, len(arr))
    for i, v := range arr {
        pairs[i].val = v
        pairs[i].ones = binaryOnes(v)
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones == pairs[j].ones {
            return pairs[i].val < pairs[j].val
        }
        return pairs[i].ones < pairs[j].ones
    })
    result := make([]int, len(arr))
    for i, v := range pairs {
        result[i] = v.val
    }
    return result
}

func binaryOnes(n int) int {
    ones := 0
    for n > 0 {
        n &= n - 1
        ones++
    }
    return ones
}
```

The `SortArray` function sorts the array based on the number of ones in their binary representation in ascending order. For similar number of ones, it sorts based on the decimal value. The binaryOnes function is used to count the number of ones in the binary representation of a number. The pair type is used to store the value and the number of ones for each number. The sort.Slice function is used to sort the slice of pairs based on the number of ones and the value. Finally, the result is created by extracting the values from the sorted slice of pairs. 

The time complexity of this solution is O(n log n) due to the sort operation, where n is the number of elements in the array. The space complexity is O(n) for storing the pairs. 

This solution assumes that the input array contains only non-negative integers. If the array can contain negative integers, the solution needs to be modified to handle this case. 

This solution also assumes that the input array does not contain duplicate values. If the array can contain duplicate values, the solution needs to be modified to handle this case. 

This solution is not efficient for large inputs because it uses the sort.Slice function, which has a time complexity of O(n log n). If the array is very large, a more efficient solution may be needed. 

This solution is not optimized for the specific problem, it's a general solution for the problem. If the problem has some specific constraints or requirements, the