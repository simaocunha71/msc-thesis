
func Fibfib(n int) int {
  if n == 0 {
    return 0
  }
  if n == 1 {
    return 0
  }
  if n == 2 {
    return 1
  }
  a, b, c := 0, 0, 1
  var next int
  for i := 3; i <= n; i++ {
    next = a + b + c
    a, b, c = b, c, next
  }
  return next
}

// The function works by initializing a, b, and c to the first three numbers in the sequence.
// Then it enters a loop that continues until it has computed the n-th number in the sequence.
// In each iteration of the loop, it computes the next number as the sum of the previous three numbers,
// and then it updates the values of a, b, and c to the last two numbers and the new number, respectively.
// Finally, it returns the n-th number in the sequence.

func main() {
  fmt.Println(Fibfib(1))  // Output: 0
  fmt.Println(Fibfib(5))  // Output: 4
  fmt.Println(Fibfib(8))  // Output: 24
}

// This program will output:
// 0
// 4
// 24
// which are the expected results.

// This program uses a dynamic programming approach to compute the n-th number in the Fibfib sequence.
// The time complexity is O(n) because it only needs to loop through the sequence once.
// The space complexity is O(1) because it only needs to keep track of the last three numbers in the sequence.
// This makes it an efficient solution.

```

This solution is efficient because it only keeps track of the last three numbers in the sequence, and it only needs to loop through the sequence once. Therefore, the time complexity is O(n) and the space complexity is O(1).

The solution can be optimized further by using memoization to store the computed Fibfib numbers and avoid redundant calculations. However, this would increase the space complexity to O(n).

Please