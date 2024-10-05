
// Initialize maximum element to first element of the list.
max := l[0]

// Iterate over the list and find maximum element.
for _, v := range l {
    if v > max {
        max = v
    }
}

return max
}

// Usage example:
l := []int{1, 2, 3}
fmt.Println(MaxElement(l))

l = []int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}
fmt.Println(MaxElement(l))


// Output:
// 3
// 123

In this solution, we find maximum element in the list by iterating over the list and comparing each element to the current maximum element. If a greater element is found, the maximum element is updated. After iterating over all elements in the list, the maximum element is returned.

To use this solution, you can call the `MaxElement` function with your list as an argument. The function will return the maximum element in the list.

In the provided usage examples, we demonstrate how to use the `MaxElement` function with two different lists: `[1, 2, 3]` and `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]`. The maximum element in each list is printed using the `fmt.Println` function.

The output of the program is:

```
3
123
```

This means that the maximum element in the first list is `3` and the maximum element in the second list is `123`.




























































































```go
package main

import (
	"fmt"
)

