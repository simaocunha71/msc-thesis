Here is the solution:

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
        str := strconv.Itoa(num)
        sum := 0
        for _, c := range str {
            sum += int(c - '0')
        }
        pairs[i] = pair{num, sum, i}
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].sum != pairs[j].sum {
            return pairs[i].sum < pairs[j].sum
        }
        return pairs[i].idx < pairs[j].idx
    })
    result := make([]int, len(nums))
    for i, pair := range pairs {
        result[i] = pair.num
    }
    return result
}
```



This function creates a new type `pair` to hold the original number, the sum of its digits, and its original index in the list. It then creates a slice of these pairs and sorts it based on the sum of the digits and the original index. The sorted slice is then converted back to a slice of integers and returned. 

The `sort.Slice` function is used to sort the slice of pairs. It takes a function that compares two pairs and returns `true` if the first pair should come before the second in the sorted order. 

In this case, the comparison function first checks if the sums of the digits of the two pairs are different. If they are, it returns `true` if the sum of the first pair is less than the sum of the second. If the sums are the same, it returns `true` if the original index of the first pair is less than the original index of the second. 

This ensures that the pairs are sorted first by the sum of their digits, and then