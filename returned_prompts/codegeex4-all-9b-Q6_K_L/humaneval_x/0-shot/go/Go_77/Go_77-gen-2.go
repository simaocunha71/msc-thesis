```go
func Iscube(a int) bool {
    if a == 0 {
        return true
    }
    root := int(math.Pow(float64(a), 1.0/3.0))
    return root*root*root == a
}
```
This function first checks if the input is zero, in which case it returns true. Then it calculates the cube root of the input using `math.Pow` and casts the result to an integer. Finally, it checks if the cube of the root is equal to the input and returns the result.