Here is the Go solution for the problem:

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
        strNum := strconv.Itoa(num)
        sum := 0
        for _, c := range strNum {
            sum += int(c - '0')
        }
        pairs[i] = pair{num, sum, i}
    }
    
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].sum < pairs[j].sum {
            return true
        }
        if pairs[i].sum > pairs[j].sum {
            return false
        }
        return pairs[i].idx < pairs[j].idx
    })
    
    result := make([]int, len(nums))
    for _, pair := range pairs {
        result[pair.idx] = pair.num
    }
    
    return result
}
```

This function works by first converting each number to a string, then calculating the sum of its digits. It then stores each number, its sum of digits, and its original index in a slice of structs. This slice is then sorted based on the sum of digits and the original index. Finally, it constructs the result slice by taking the numbers from the sorted slice and placing them back in their original positions. The result is a slice of numbers sorted by the sum of their digits, with ties broken by the original index. 