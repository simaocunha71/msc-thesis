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
    var pairs []pair
    for i, num := range nums {
        str := strconv.Itoa(abs(num))
        sum := 0
        for _, c := range str {
            sum += int(c - '0')
        }
        pairs = append(pairs, pair{num, sum, i})
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].sum != pairs[j].sum {
            return pairs[i].sum < pairs[j].sum
        }
        return pairs[i].idx < pairs[j].idx
    })
    result := make([]int, 0, len(pairs))
    for _, pair := range pairs {
        result = append(result, pair.num)
    }
    return result
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```



Explanation:
We create a new type `pair` that holds the original number, the sum of its digits, and its index in the original array. We then iterate over the input array, calculate the sum of the digits for each number, and store the results in the `pairs` array.

Next, we sort the `pairs` array using the `sort.Slice` function. We define a comparison function that first checks if the sums of the digits are different. If they are, it returns `true` if the first sum is less than the second sum, and `false` otherwise. If the sums are the same, it returns `true` if the first index is less than the second index, and `false` otherwise.

Finally, we create a new array `result` and iterate over the `pairs` array. For each pair, we append the original number to the `result` array