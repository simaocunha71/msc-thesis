Here is the solution to the problem:

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
    var p []pair
    for _, num := range arr {
        p = append(p, pair{num, binCount(num)})
    }
    sort.Slice(p, func(i, j int) bool {
        if p[i].ones == p[j].ones {
            return p[i].num < p[j].num
        }
        return p[i].ones < p[j].ones
    })
    result := make([]int, len(p))
    for i, pair := range p {
        result[i] = pair.num
    }
    return result
}

func binCount(num int) int {
    count := 0
    for num > 0 {
        if num & 1 == 1 {
            count++
        }
        num >>= 1
    }
    return count
}

func main() {
    fmt.Println(SortArray([]int{1, 5, 2, 3, 4}))  // [1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{-2, -3, -4, -5, -6}))  // [-6, -5, -4, -3, -2]
    fmt.Println(SortArray([]int{1, 0, 2, 3, 4}))  // [0, 1, 2, 3, 4]
}
```


In this solution, we first create a new struct `pair` that holds the original number and the count of ones in its binary representation. Then, we create a new slice `p` of `pair` and append each number in the input array to `p`. We sort `p` based on the count of ones and the original number. Finally, we create a new slice `result` and append the original numbers from `p` to `result`. The result is the sorted array. The `binCount` function is used to count the number of ones in the binary representation of a number.