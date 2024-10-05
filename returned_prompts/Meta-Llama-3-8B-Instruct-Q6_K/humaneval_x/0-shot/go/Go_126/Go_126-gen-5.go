```go
package main

import (
    "fmt"
    "sort"
)

func IsSorted(lst []int) bool {
    if len(lst) == 0 {
        return true
    }
    duplicates := make(map[int]bool)
    for i := 1; i < len(lst); i++ {
        if lst[i] <= lst[i-1] {
            return false
        }
        if duplicates[lst[i]] {
            return false
        }
        duplicates[lst[i]] = true
    }
    return true
}

func main() {
    fmt.Println(IsSorted([]int{5})) // true
    fmt.Println(IsSorted([]int{1, 2, 3, 4, 5})) // true
    fmt.Println(IsSorted([]int{1, 3, 2, 4, 5})) // false
    fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6})) // true
    fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6, 7})) // true
    fmt.Println(IsSorted([]int{1, 3, 2, 4, 5, 6, 7})) // false
    fmt.Println(IsSorted([]int{1, 2, 2, 3, 3, 4})) // true
    fmt.Println(IsSorted([]int{1, 2, 2, 2, 3, 4})) // false
}
```
This function works by iterating over the list and checking if each element is greater than the previous one. If it finds an element that is not greater, it returns false. It also keeps track of the elements it has seen so far in a map, and if it sees an element that is already in the map, it returns false. If it makes it through the whole list without finding any non-increasing elements or duplicates, it returns true. The time complexity of this function is O(n), where n is the length of the list, because it makes a single pass through the list. The space complexity is O(n) because in the worst case it has to store every element in the map. The sort package is not used in this solution, but it could be used to sort the list and then check if it is sorted, which would have a time complexity of O(n log n) and a space complexity of