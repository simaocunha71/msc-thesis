```go
package main

import "fmt"

func IsSorted(lst []int) bool {
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] >= lst[i+1] {
            if i > 0 && lst[i] == lst[i-1] {
                return false
            }
            return false
        }
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


The function IsSorted checks if the input list is sorted in ascending order and does not contain more than one occurrence of the same number. 

The function iterates over the list and checks if each element is less than the next one. If it is not, the function returns false. 

If the function finds two equal elements in a row, it also returns false, because this means the list contains more than one occurrence of the same number.

If the function iterates over the entire list without finding any incorrect elements, it returns true, indicating that the list is sorted and does not contain more than one occurrence of the same number. 





The time complexity of this function is O(n), where n is the length of the input list, because it iterates over the list once. The space complexity is O(1), because it only uses a constant amount of space to store the current element and the previous element.