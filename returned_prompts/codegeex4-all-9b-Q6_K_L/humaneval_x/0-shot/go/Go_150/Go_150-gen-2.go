The problem is that you are not checking if the number is prime at all. You are just returning x for all cases. Here is the corrected code:

```go
func XOrY(n, x, y int) int {
    for i := 2; i < n; i++ {
        if n%i == 0 {
            return y
        }
    }
    return x
}
```
This code will check if the number is prime by looping from 2 to n-1 and checking if n is divisible by any number in that range. If it is, then it is not a prime number and the function will return y. If it is not divisible by any number in that range, then it is a prime number and the function will return x.