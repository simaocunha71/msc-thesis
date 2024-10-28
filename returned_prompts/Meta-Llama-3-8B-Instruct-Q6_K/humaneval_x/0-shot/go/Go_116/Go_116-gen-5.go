Here is a solution to the problem using Go programming language:

```go
import (
    "fmt"
    "sort"
)

func SortArray(arr []int) []int {
    type pair struct {
        num  int
        ones int
    }

    pairs := make([]pair, len(arr))
    for i, num := range arr {
        pairs[i].num = num
        pairs[i].ones = binCount(num)
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones == pairs[j].ones {
            return pairs[i].num < pairs[j].num
        }
        return pairs[i].ones < pairs[j].ones
    })

    result := make([]int, len(pairs))
    for i, pair := range pairs {
        result[i] = pair.num
    }
    return result
}

func binCount(n int) int {
    count := 0
    for n > 0 {
        n &= n - 1
        count++
    }
    return count
}
```

This solution defines a struct `pair` to hold each number and its count of ones in binary representation. Then it creates a slice of `pair` and sorts it based on the number of ones in ascending order. If two numbers have the same number of ones, it sorts them based on their decimal value. Finally, it creates a new slice to hold the sorted numbers and returns it. The function `binCount` counts the number of ones in the binary representation of a number. 

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the size of the input array. The space complexity is O(n) for storing the pairs and the result. 