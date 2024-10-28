Here is the solution in Go:

```go
import (
    "sort"
    "strconv"
)

// Write a function which sorts the given list of integers
// in ascending order according to the sum of their digits.
// Note: if there are several items with similar sum of their digits,
// order them based on their index in original list.
// 
// For example:
// >>> OrderByPoints([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
// >>> OrderByPoints([]) == []
func OrderByPoints(nums []int) []int {
    type pair struct {
        num int
        sum int
        idx int
    }
    
    pairs := make([]pair, len(nums))
    for i, num := range nums {
        sum := sumOfDigits(num)
        pairs[i] = pair{num, sum, i}
    }
    
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].sum != pairs[j].sum {
            return pairs[i].sum < pairs[j].sum
        }
        return pairs[i].idx < pairs[j].idx
    })
    
    result := make([]int, len(nums))
    for _, pair := range pairs {
        result[pair.idx] = pair.num
    }
    
    return result
}

func sumOfDigits(num int) int {
    sum := 0
    for num != 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}
```


In this solution, we first create a new type `pair` which holds the original number, the sum of its digits, and its original index. Then we create a slice of `pair`s, where each `pair` contains the original number, the sum of its digits, and its original index.

Next, we use the `sort.Slice` function to sort the `pairs` slice. The sorting function compares two `pair`s based on their sums of digits. If the sums are equal, it compares their original indices. This ensures that the numbers with the same sum of digits are ordered based on their original indices.

Finally, we create a new slice `result` and copy the numbers from the `pairs` slice to `result`, using the original indices to determine the order. The `result` slice is then returned. The `sumOfDigits` function is used to calculate the sum