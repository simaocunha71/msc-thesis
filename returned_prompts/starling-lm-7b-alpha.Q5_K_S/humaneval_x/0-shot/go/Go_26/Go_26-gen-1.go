
To solve this problem, you can use a map to track the elements that have been seen so far. Then you can iterate through the input slice and check if the element has been seen before. If it hasn't, add it to a result slice. Here's a sample implementation:

```go
package main

import "fmt"

func RemoveDuplicates(numbers []int) []int {
    result := make([]int, 0)
    seen := make(map[int]struct{})

    for _, n := range numbers {
        if _, ok := seen[n]; !ok {
            seen[n] = struct{}{}
            result = append(result, n)
        }
    }

    return result
}
```

In this code, `seen` is a map that is used to keep track of the elements that have been seen so far. The keys of the map are the unique elements, and the values are of type `struct{}`. This is a zero-size type, so it doesn't take any space in memory.

The `for` loop iterates through the input slice `numbers`. For each element `n`, it checks if `n` has been seen before by checking if `seen[n]` exists. If `seen[n]` doesn't exist, it means that `n` has not been seen, so we add it to the result slice and also add it to the `seen` map.

Finally, the function returns the result slice, which contains the unique elements in the same order as they appear in the input slice.

You can use this function like this:

```go
package main

import "fmt"

func main() {
    fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}
```

This will output `[1, 3, 4]`, which is the result after removing the duplicate elements.

Hope this helps!

```go
package main

import "fmt"

func main() {
    fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}
```

This will output `[1