
```go
func Fibfib(n int) int {
    if n == 0 || n == 1 {
        return 0
    } else if n == 2 {
        return 1
    }

    a, b, c := 0, 1, 1
    for i := 3; i <= n; i++ {
        c = a + b
        a, b = b, c
    }
    return c
}
```

Explanation:
The Fibfib number sequence is similar to the Fibonacci sequence, so we can use the same method to calculate it, that is, we can use the loop to calculate all the Fibfib numbers up to n and return the nth Fibfib number. The time complexity of this method is O(n).

First, we initialize three variables a, b, c to 0, 1, 1, respectively. Then, we use a for loop to calculate the Fibfib numbers from 3 to n and update the variables a, b, c in each step. Finally, we return the value of c, which is the nth Fibfib number.

For example, if we want to calculate the 8th Fibfib number, we initialize a, b, c to 0, 1, 1. Then, we enter the for loop and calculate the Fibfib numbers from 3 to 8. In the 4th step, a becomes 1, b becomes 1, and c becomes 2. In the 5th step, a becomes 1, b becomes 2, and c becomes 3. In the 6th step, a becomes 2, b becomes 3, and c becomes 5. In the 7th step, a becomes 3, b becomes 5, and c becomes 8. In the 8th step, a becomes 5, b becomes 8, and c becomes 13. Finally, we return the value of c, which is the 8th Fibfib number, 13.

```
// The Fibfib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
// Fibfib(0) == 0