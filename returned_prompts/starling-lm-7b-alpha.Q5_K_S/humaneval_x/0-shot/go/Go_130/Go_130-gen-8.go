
```go
func Tri(n int) []float64 {
    if n == 0 {
        return []float64{0}
    }
    res := make([]float64, n+1)
    res[0] = 0
    res[1] = 1
    res[2] = 3
    if n > 2 {
        for i := 3; i <= n; i++ {
            if i%2 == 1 {
                res[i] = res[i-1] + res[i-2] + res[i+1]
            } else {
                res[i] = 1 + i/2
            }
        }
    }
    return res
}
```

Explanation:
This problem can be solved using dynamic programming.
As you can see, the Tribonacci sequence can be solved using the following recurrence relation:

- Tri(1) = 3
- Tri(n) = 1 + n / 2, if n is even.
- Tri(n) =  Tri(n - 1) + Tri(n - 2) + Tri(n + 1), if n is odd.

So, we can use the dynamic programming to solve this problem.

Firstly, we initialize the first three elements of the sequence, then we use a loop to calculate the next elements.
If the number is odd, we calculate the element as the sum of the previous three elements; if the number is even, we calculate the element as 1 + n / 2.

Finally, we return the result.

The time complexity of this method is O(n), and the space complexity is also O(n), as we need to use an array to store the result.

In the above code, we use a for loop to calculate the elements of the Tribonacci sequence, and use a variable to store the result.

```go
for i := 3; i <= n; i++ {
    if i%2 == 1 {
        res[i] = res[i-1] + res[i-2] + res[i+1]
    } else {
        res[i] = 1 + i/2
   