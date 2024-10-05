
The function SumToN(n int) int calculates the sum of all numbers from 1 to n. The formula for this is n*(n+1)/2. Here is the implementation in Go:

```go
func SumToN(n int) int {
    return n * (n + 1) / 2
}
```

This function takes an integer n as an argument and returns the sum of all numbers from 1 to n. It uses the mathematical formula for the sum of an arithmetic series, which is n*(n+1)/2. This formula is efficient and accurate for calculating the sum of a large range of numbers. 

For example, if you call SumToN(30), it will return 465, which is the sum of all numbers from 1 to 30. If