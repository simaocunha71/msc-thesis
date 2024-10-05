The task is to write a function that returns true if a number x is a simple power of n and false in other cases. A simple power of n is defined as n raised to the power of an integer.

Here is a possible solution in Go:
```go
func IsSimplePower(x int, n int) bool {
    if n <= 0 {
        return false
    }
    i := 1
    for {
        pow := int(math.Pow(float64(n), float64(i)))
        if pow == x {
            return true
        }
        if pow > x {
            return false
        }
        i++
    }
}
```
This function uses a loop to calculate the power of n for increasing values of i. It checks if the calculated power is equal to x, and if it is, it returns true. If the calculated power exceeds x, it returns false. If the function reaches this point, it means that x is not a simple power of n, so it returns false.

The function also checks if n is less than or equal to 0, in which case it returns false, since a simple power of a non-positive number does not make sense.

You can test this function with the examples you provided:
```go
fmt.Println(IsSimplePower(1, 4)) // true
fmt.Println(IsSimplePower(2, 2)) // true
fmt.Println(IsSimplePower(8, 2)) // true
fmt.Println(IsSimplePower(3, 2)) // false
fmt.Println(IsSimplePower(3, 1)) // false
fmt.Println(IsSimplePower(5, 3)) // false
```
I hope this helps! Let me know if you have any questions.