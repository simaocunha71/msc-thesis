
The given function is a simple arithmetic progression that calculates the sum of numbers from 1 to n. The formula for this is:

n * (n + 1) / 2

Here is the implementation in Go:

```go
func SumToN(n int) int {
    return n * (n + 1) / 2
}
```

You can test this function with the given examples:

```go
fmt.Println(SumToN(30)) // 465
fmt.Println(SumToN(100)) // 5050
fmt.Println(SumToN(5)) // 15
fmt.Println(SumToN(10)) // 55
fmt.Println(SumToN(1)) // 1
```
