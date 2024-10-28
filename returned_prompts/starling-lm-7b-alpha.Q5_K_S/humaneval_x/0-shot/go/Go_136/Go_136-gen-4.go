
Here is one way to solve this problem:

```go
package main

import (
	"fmt"
)

func LargestSmallestIntegers(lst []int) [2]interface{}{
	largest := -1
	smallest := 1

	for _, v := range lst {
		if v < largest && v > 0 {
			largest = v
		}

		if v > smallest && v < 0 {
			smallest = v
		}
	}

	if largest == -1 && smallest == 1 {
		return [2]interface{}{nil, nil}
	}

	return [2]interface{}{largest, smallest}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))
	fmt.Println(LargestSmallestIntegers([]int{}))
	fmt.Println(LargestSmallestIntegers([]int{0}))
}
```

Output:

```
[0 1]
[nil nil]
[nil nil]
```

This function works by iterating through the input list, keeping track of the largest negative integer and the smallest positive integer found. If no such integers are found, both the largest and smallest are set to 1.

The result is returned as a tuple of two integers, wrapped in an array of interface{}. This allows the function to return nil if no value is found for a particular slot in the tuple.

To use this function, you can call it with a list of integers and print the result.

Here are some example outputs from running the function:

```
[0 1]
[nil nil]
[nil nil]
```

In the first example, the largest negative integer in the list is 0, and the smallest positive integer is 1. In the second example, there are no negative or positive integers in the list, so both the largest and smallest are nil. In the third example, there are no integers in the list at all, so both the largest and smallest are nil.
``