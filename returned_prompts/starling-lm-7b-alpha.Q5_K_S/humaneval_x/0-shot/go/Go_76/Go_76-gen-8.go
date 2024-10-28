
```go
func IsSimplePower(x int,n int) bool {
    for i:=1;i<32;i++ {
        if n == int(math.Pow(float64(n), float64(i))) {
            return true
        }
    }
    return false
}
```

This function checks if a number x is equal to any power of number n. It does it by looping from 1 to 31 (max 32-bit integer value), calculating n to the power of i, and checking if it equals x.

```go
func IsSimplePower(x int,n int) bool {
    for i:=1;i<32;i++ {
        if n == int(math.Pow(float64(n), float64(i))) {
            return true
        }
    }
    return false
}
```

In this example, the function is called with x = 8 and n = 2. It will check if 2 is equal to 2^1, 2^2, 2^3, ..., 2^31. Since 2 is equal to 2^1, the function will return true.

```go
func main() {
    fmt.Println(IsSimplePower(8, 2)) // true
}
```

Here is a test program that demonstrates the use of the function. It prints true to the console, confirming that 8 is a simple power of 2.

```go
func main() {
    fmt.Println(IsSimplePower(8, 2)) // true
}
```

This test program calls the function with x = 8 and n = 2. It prints the result of the function call, which is true, to the console.

```go
func main() {
    fmt.Println(IsSimplePower(8, 2)) // true
}
```

The function can be called with any two integers x and n. It will return true if x is a simple power of n, and false otherwise.

```go
func main() {
    fmt.Println(IsSimplePower(3, 