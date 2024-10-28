To determine whether a given set of three sides can form a right-angled triangle,
you must check if the square of the longest side is equal to the sum of the squares
of the other two sides. If it is, then the three sides can form a right-angled triangle.

Here is a step-by-step walkthrough of the solution:

1. Initialize a variable called result to false. This variable will be used
to store whether the three sides can form a right-angled triangle or not.
2. Sort the three sides in ascending order. Let us assume that the sorted sides
are a, b, and c, where a <= b <= c.
3. Check if (c*c) == (a*a + b*b). If it is, then the three sides can form a
right-angled triangle, and set the result variable to true. Otherwise, set the
result variable to false.
4. Return the result variable.

In the provided code, the RightAngleTriangle function takes three integer
arguments a, b, and c. Inside the function, the three sides are sorted in
ascending order using the sort.Ints function. Then, the condition (c*c) == (a*a + b*b)
is checked. If it holds true, the result variable is set to true using the assignment
operator (=). Otherwise, the result variable is set to false using the assignment
operator (=). Finally, the result variable is returned.

Here is the code:

```go
package main

import (
	"fmt"
	"sort"
)

func RightAngleTriangle(a, b, c int) bool {
	result := false
	var sides []int = []int{a, b, c}
	sort.Ints(sides)
	if (sides[2] * sides[2]) == (sides[0] * sides[0] + sides[1] * sides[1]) {
		result = true
	}
	return result
}

func main() {
	fmt.Println(RightAngleTriangle(3, 4, 5))
	fmt.Println(RightAngleTriangle(1, 2, 3))
}
```

When you run the code