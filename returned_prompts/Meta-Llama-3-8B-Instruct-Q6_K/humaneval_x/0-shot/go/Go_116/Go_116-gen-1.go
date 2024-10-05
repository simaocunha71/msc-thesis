```go
package main

import (
    "fmt"
    "sort"
)

// In this Kata, you have to sort an array of non-negative integers according to
// number of ones in their binary representation in ascending order.
// For similar number of ones, sort based on decimal value.
// 
// It must be implemented like this:
// >>> SortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
// >>> SortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
// >>> SortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]

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
    result := make([]int, len(pairs))
    for i, pair := range pairs {
        result[i] = pair.num
    }
    return result
}

func binOnes(n int) int {
    count := 0
    for n > 0 {
        n &= (n - 1)
        count++
    }
    return count
}

func main() {
    fmt.Println(SortArray([]int{1, 5, 2, 3, 4})) // [1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{-2, -3, -4, -5, -6})) // [-6, -5, -4, -3, -2]
    fmt.Println(SortArray([]int{1, 0, 2, 3, 4})) // [0, 1, 2, 3, 4]
}
```
In this solution, we create a custom type `pair` to store the number and the count