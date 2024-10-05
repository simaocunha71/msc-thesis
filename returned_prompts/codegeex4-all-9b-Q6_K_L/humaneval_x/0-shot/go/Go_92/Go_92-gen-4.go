```go
func AnyInt(x, y, z interface{}) bool {
    // Convert all inputs to int
    a := int(x.(float64))
    b := int(y.(float64))
    c := int(z.(float64))

    // Check if any of the numbers is equal to the sum of the other two
    return a == b+c || b == a+c || c == a+b
}
```
