```go
package main
import "fmt"

func PairsSumToZero(l []int) bool {
    set := make(map[int]bool)
    for _, v := range l {
        if _, ok := set[-v]; ok {
            return true
        }
        set[v] = true
    }
    return false
}

func main() {
    fmt.Println(PairsSumToZero([]int{1, 3, 5, 0})) // false
    fmt.Println(PairsSumToZero([]int{1, 3, -2, 1})) // false
    fmt.Println(PairsSumToZero([]int{1, 2, 3, 7})) // false
    fmt.Println(PairsSumToZero([]int{2, 4, -5, 3, 5, 7})) // true
    fmt.Println(PairsSumToZero([]int{1})) // false
}
```


Explanation:
The function PairsSumToZero checks if there are two distinct elements in the list that sum to zero. It does this by creating a set of the elements it has seen so far. If it ever sees an element that is the negation of an element it has seen before, it returns true, because it has found two elements that sum to zero. If it gets through the entire list without finding such a pair, it returns false.

This function runs in O(n) time, where n is the length of the input list, because it makes one pass through the list. It uses O(n) space to store the set of elements it has seen. The space usage could be reduced to O(1) by using a boolean array to keep track of the elements it has seen, but this would increase the time complexity to O(n^2) because it would have to check every element against every other element. The current solution is a good trade-off between space and time complexity.