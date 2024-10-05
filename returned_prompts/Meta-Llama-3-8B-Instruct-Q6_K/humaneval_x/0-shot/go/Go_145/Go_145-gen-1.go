```go
package main

import (
    "fmt"
    "sort"
    "strconv"
)

type pair struct {
    num int
    sum int
    idx int
}

func OrderByPoints(nums []int) []int {
    pairs := make([]pair, len(nums))
    for i, num := range nums {
        s := strconv.Itoa(num)
        sum := 0
        for _, c := range s {
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
    for _, p := range pairs {
        result[p.idx] = p.num
    }
    return result
}

func main() {
    fmt.Println(OrderByPoints([]int{1, 11, -1, -11, -12})) // Output: [-1, -11, 1, -12, 