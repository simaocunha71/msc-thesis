
    type pair struct {
        idx  int
        sum  int
        num  int
    }

    pairs := make([]pair, len(nums))

    for i, num := range nums {
        sum := 0
        for num != 0 {
            digit := num % 10
            sum += digit
            num /= 10
        }
        pairs[i] = pair{i, sum, nums[i]}
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].sum != pairs[j].sum {
            return pairs[i].sum < pairs[j].sum
        }
        return pairs[i].idx < pairs[j].idx
    })

    sortedNums := make([]int, len(nums))
    for i, pair := range pairs {
        sortedNums[i] = pair.num
    }

    return sortedNums
}
```

## Answer 2:
```go
package main

import (
	"fmt"
	"sort"
	"strconv"
)

func OrderByPoints(nums []int) []int {

	sort.Slice(nums, func(i, j int) bool {
		sumI, sumJ := 0, 0
		for _, digitStr := range strconv.Itoa(nums[i]) {
			digit, _ := strconv.Atoi(string(digitStr))
			sumI += digit
		}
		for _, digitStr := range strconv.Itoa(nums[j]) {
			digit, _ := strconv.Atoi(string(digitStr))
			sumJ += digit
		}
		if sumI != sumJ {
			return sumI < sumJ
		}
		return nums[i] < nums[j]
	})

	return nums
}

func main() {
	fmt.Println(OrderByPoints([]int{1, 11, -1, -11, -12})) 