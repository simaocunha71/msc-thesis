```go
func AnyInt(x, y, z interface{}) bool {
    if x == nil || y == nil || z == nil {
        return false
    }

    a, ok1 := x.(int)
    b, ok2 := y.(int)
    c, ok3 := z.(int)

    if !ok1 || !ok2 || !ok3 {
        return false
    }

    if a == b + c || b == a + c || c == a + b {
        return true
    }

    return false
}
```