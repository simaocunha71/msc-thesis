Here is a solution for the problem:

```go
import (
    "sort"
    "strconv"
)

func OrderByPoints(nums []int) []int {
    type pair struct {
        num int
        sum int
        idx int
    }
    pairs := make([]pair, len(nums))
    for i, num := range nums {
        s := strconv.Itoa(num)
        sum := 0
        for _, c := range s {
            sum += int(c - '0')
        }
        pairs[i].num = num
        pairs[i].sum = sum
        pairs[i].idx = i
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].sum != pairs[j].sum {
            return pairs[i].sum < pairs[j].sum
        }
        return pairs[i].idx < pairs[j].idx
    })
    result := make([]int, len(pairs))
    for i, p := range pairs {
        result[i] = p.num
    }
    return result
}
```

The function `OrderByPoints` takes a list of integers as input and returns the sorted list. It first creates a slice of pairs, where each pair contains a number, the sum of its digits, and its original index. Then it sorts this slice based on the sum of digits and the original index. Finally, it creates a new slice with the sorted numbers and returns it.

The `sort.Slice` function is used to sort the slice of pairs. It takes a function as an argument, which is used to compare two pairs. In this case, the function compares two pairs based on their sums of digits. If the sums are equal, it compares the original indices. This ensures that if there are several items with similar sum of their digits, they are ordered based on their index in the original list.

The time complexity of this solution is O(n log n) due to the sort operation, where n is the length of the input list. The space complexity is O(n) for storing the pairs and the result.