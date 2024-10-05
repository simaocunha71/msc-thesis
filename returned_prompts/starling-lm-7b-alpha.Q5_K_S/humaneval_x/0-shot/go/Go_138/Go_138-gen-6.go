To determine if a given number can be written as the sum of exactly 4 positive even numbers, we can use a backtracking approach. Here's a step-by-step breakdown of the solution:

1. Initialize a variable "target" to store the given number "n".
2. Create a function called "backtrack" that takes the current sum, the target, and the current index as input.
3. If the current index is 4 (i.e., we have considered all the even numbers), check if the current sum is equal to the target. If it is, return True; otherwise, return False.
4. If the current index is 0, return False (since we haven't considered any even numbers yet).
5. If the current index is greater than the target, return False (since the current sum exceeds the target).
6. Generate the next even number by taking the current index as the base and multiplying it by 2. Add this even number to the current sum.
7. Recursively call the "backtrack" function with the updated current sum, target, and incremented index.
8. If the recursive call returns True, return True; otherwise, return False.
9. If the current sum becomes larger than the target, backtrack and consider the next even number by resetting the current sum to the previous sum minus the current even number.
10. Repeat steps 6-9 until all possible combinations of even numbers are considered.

Here's the code implementation of the solution:

```go
package main

import "fmt"

func IsEqualToSumEven(n int) bool {
    target := n
    return backtrack(0, target, 0)
}

func backtrack(sum, target, index int) bool {
    if index == 4 {
        return sum == target
    }
    if index == 0 {
        return false
    }
    if sum > target {
        return false
    }
    next := index * 2
    if backtrack(sum + next, target, index + 1) {
        return true
    }
    if sum + next > target {
        backtrack(sum-next, target, index)
    }
    return false
}
```

To use