```go
func AnyInt(x, y, z interface{}) bool {
    if reflect.TypeOf(x).Kind() != reflect.Int || reflect.TypeOf(y).Kind() != reflect.Int || reflect.TypeOf(z).Kind() != reflect.Int {
        return false
    }
    if (x.(int)+y.(int) == z.(int)) || (x.(int)+z.(int) == y.(int)) || (y.(int)+z.(int) == x.(int)) {
        return true
    }
    return false
}
```
