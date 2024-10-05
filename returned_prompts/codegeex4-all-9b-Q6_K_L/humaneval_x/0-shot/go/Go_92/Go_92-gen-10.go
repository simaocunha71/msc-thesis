```go
func AnyInt(x, y, z interface{}) bool {
    switch x := x.(type) {
    case int:
        if y.(int)+z.(int) == x || x+y.(int) == z.(int) || x+z.(int) == y.(int) {
            return true
        }
    case float64:
        if y.(float64)+z.(float64) == x || x+y.(float64) == z.(float64) || x+z.(float64) == y.(float64) {
            return true
        }
    }
    return false
}
```