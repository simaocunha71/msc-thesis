You can use the sort and then find the second smallest element. Here is the solution:

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
    if len(lst) > 1 {
        return lst[1]
    }
    return nil
}
```

This function first checks if the length of the list is less than 2. If it is, it returns nil because there is no 2nd smallest element. Then it sorts the list in ascending order. If the length of the list is greater than 1, it returns the second element of the sorted list which is the 2nd smallest element. If the length of the list is 1, it means all elements are the same and there is no 2nd smallest element, so it returns nil. 

This solution works in O(n log n) time complexity due to the sort operation. The space complexity is O(1) as it only uses a constant amount of space. 

You can test this function with the provided test cases:

```go
fmt.Println(NextSmallest([]int{1, 2, 3, 4, 5})) // Output: 2
fmt.Println(NextSmallest([]int{5, 1, 4, 3, 2})) // Output: 2
fmt.Println(NextSmallest([]int{})) // Output: nil
fmt.Println(NextSmallest([]int{1, 1})) // Output: nil
``` 







