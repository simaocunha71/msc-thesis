
To solve this problem, you can use the formula for the sum of the first n natural numbers, which is n*(n+1)/2. Here's how you can implement the SumToN function:

```go
func SumToN(n int) int {
    return n * (n + 1) / 2
}
```

Now you can use this function to calculate the sum of the first n natural numbers. Here are some test cases:

```go
fmt.Println(SumToN(30)) // Output: 465
fmt.Println(SumToN(100)) // Output: 5050
fmt.Println(SumToN(5)) // Output: 15
fmt.Println(SumToN(10)) // Output: 55
fmt.Println(SumToN(1)) // Output: 1
```

In each test case, the SumToN function is called with a different value for n. The result is printed to the console using the fmt.Println function.

Note: The formula n*(n+1)/2 works for all non-negative integers n, including 0. It's a useful formula to know when you need to calculate the sum of the first n natural numbers.

```go
```

```
```