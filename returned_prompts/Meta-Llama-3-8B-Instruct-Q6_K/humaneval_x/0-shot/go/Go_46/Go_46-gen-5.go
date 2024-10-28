```go
func Fib4(n int) int {
    if n < 1 {
        return 0
    }
    if n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }
    fib4 := [5]int{0, 0, 2, 0, 2}
    for i := 4; i <= n; i++ {
        fib4[i%5] = (fib4[(i-1)%5] + fib4[(i-2)%5] + fib4[(i-3)%5] + fib4[(i-4)%5]) % 3
    }
    return fib4[n%5]
}
```
The idea is to use a fixed-size array to store the last 5 elements of the sequence. The modulus operation is used to handle the wrap-around effect when the sequence wraps around the array. The final result is then obtained by looking up the nth element in the array. This approach avoids the need for recursion and has a time complexity of O(1) since it only depends on the input n.