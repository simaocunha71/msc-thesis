Here is the solution:

```go
import (
    "fmt"
    "sort"
)

func SortArray(arr []int) []int {
    type pair struct {
        num int
        ones int
    }
    
    pairs := make([]pair, len(arr))
    for i, num := range arr {
        pairs[i].num = num
        pairs[i].ones = binOnes(num)
    }
    
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones != pairs[j].ones {
            return pairs[i].ones < pairs[j].ones
        }
        return pairs[i].num < pairs[j].num
    })
    
    result := make([]int, len(arr))
    for i, pair := range pairs {
        result[i] = pair.num
    }
    
    return result
}

func binOnes(n int) int {
    count := 0
    for n > 0 {
        n &= n - 1
        count++
    }
    return count
}
```

In this solution, we create a new type `pair` that has two fields: `num` to store the original number and `ones` to store the number of ones in its binary representation. We then create a slice of `pair` and fill it with the original numbers and the number of ones in their binary representation.

We use the `sort.Slice` function to sort the slice of `pair` based on the number of ones and then the original numbers. If the number of ones is the same, we sort based on the original numbers.

Finally, we create a new slice to store the sorted numbers and fill it with the `num` field of the `pair` slice.

The `binOnes` function is used to count the number of ones in the binary representation of a number. It uses the bitwise AND operator (`&`) to remove the least significant bit until there are no more ones left. The number of iterations is the number of ones.