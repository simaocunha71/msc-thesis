Here is the solution in Go:

```go
import (
    "math"
    "sort"
)

func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    for i := 1; i < len(lst); i++ {
        if lst[i] > lst[0] {
            return lst[i]
        }
    }
    return nil
}
```

Explanation:
- First, we check if the length of the list is less than 2. If it is, we return nil as there's no 2nd smallest element.
- We sort the list in ascending order.
- We iterate through the list starting from the second element (index 1). We stop when we find an element that is greater than the smallest element in the list. This element is the 2nd smallest element.
- If we reach the end of the list without finding a 2nd smallest element, we return nil.

You can test this function with the provided examples:

```go
fmt.Println(NextSmallest([]int{1, 2, 3, 4, 5})) // Output: 2
fmt.Println(NextSmallest([]int{5, 1, 4, 3, 2})) // Output: 2
fmt.Println(NextSmallest([]int{})) // Output: nil
fmt.Println(NextSmallest([]int{1, 1})) // Output: nil
```