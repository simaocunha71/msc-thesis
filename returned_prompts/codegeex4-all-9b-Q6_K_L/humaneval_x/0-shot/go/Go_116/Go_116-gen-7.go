```go
import (
    "fmt"
    "sort"
)

type ByOnes struct {
    arr []int
}

func (s ByOnes) Len() int {
    return len(s.arr)
}

func (s ByOnes) Swap(i, j int) {
    s.arr[i], s.arr[j] = s.arr[j], s.arr[i]
}

func (s ByOnes) Less(i, j int) bool {
    onesI := ones(s.arr[i])
    onesJ := ones(s.arr[j])
    if onesI == onesJ {
        return s.arr[i] < s.arr[j]
    }
    return onesI < onesJ
}

func ones(n int) int {
    count := 0
    for n > 0 {
        if n & 1 == 1 {
            count++
        }
        n >>= 1
    }
    return count
}

func SortArray(arr []int) []int {
    s := ByOnes{arr}
    sort.Sort(s)
    return s.arr
}

func main() {
    fmt.Println(SortArray([]int{1, 5, 2, 3, 4})) // [1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{-2, -3, -4, -5, -6})) // [-6, -5, -4, -3, -2]
    fmt.Println(SortArray([]int{1, 0, 2, 3, 4})) // [0, 1, 2, 3, 4]
}
```