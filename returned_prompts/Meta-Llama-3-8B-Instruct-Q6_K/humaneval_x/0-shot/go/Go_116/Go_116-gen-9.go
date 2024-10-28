Here is the solution in Go:

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
        pairs[i].ones = binOnes(num)
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones == pairs[j].ones {
            return pairs[i].num < pairs[j].num
        }
        return pairs[i].ones < pairs[j].ones
    })
    result := make([]int, len(arr))
    for i, pair := range pairs {
        result[i] = pair.num
    }
    return result
}

func binOnes(n int) int {
    ones := 0
    for n > 0 {
        if n & 1 == 1 {
            ones++
        }
        n >>= 1
    }
    return ones
}
```

This solution uses a custom struct pair to store the number and the number of ones in its binary representation. It then uses the sort.Slice function to sort the pairs. The custom comparison function first compares the number of ones, and if they are equal, it compares the decimal value. The result is then constructed from the sorted pairs. The binOnes function is used to count the number of ones in the binary representation of a number. 

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the number of elements in the input array. The space complexity is O(n) for storing the pairs and the result. 