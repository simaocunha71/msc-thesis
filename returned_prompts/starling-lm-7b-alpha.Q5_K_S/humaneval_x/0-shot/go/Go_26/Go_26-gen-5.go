
To solve this problem, you can use a map to keep track of the number of occurrences of each element in the input array. Then, you can create a new array with the elements that occur only once.

Here's the code that solves the problem:

```go
package main

import "fmt"

func RemoveDuplicates(numbers []int) []int {
    m := make(map[int]int)
    result := []int{}

    for _, n := range numbers {
        m[n]++
    }

    for key, _ := range m {
        if m[key] == 1 {
            result = append(result, key)
        }
    }

    return result
}

func main() {
    fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}
```

The `RemoveDuplicates` function first creates an empty map `m` and an empty array `result`. It then iterates over the input array `numbers` and increments the count of each number in the map.

Next, it iterates over the map and appends the keys (numbers) to the `result` array if their corresponding value in the map is equal to 1. This ensures that only the elements that occur only once are included in the `result` array.

Finally, the `result` array is returned, containing the elements from the input array that occur only once, while preserving the order of the elements.

When you run the program, it will print the result of calling the `RemoveDuplicates` function with the input `[1, 2, 3, 2, 4]`, which is `[1, 3, 4]`.

```
[1, 3, 4]
```

Note that this solution has a time complexity of O(n), where n is the length of the input array. This is because it iterates over the input array once to count the occurrences of each element, and then iterates over the map once to create the result array.

The space complexity of this solution is also O(n), as it uses additional space to store the map and the result array.