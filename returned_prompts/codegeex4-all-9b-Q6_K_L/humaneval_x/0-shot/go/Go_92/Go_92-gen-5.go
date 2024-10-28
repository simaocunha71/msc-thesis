```go
func AnyInt(x, y, z interface{}) bool {
    i := []int{x.(int), y.(int), z.(int)}
    for _, v := range i {
        if i[0]+i[1] == v || i[0]+i[2] == v || i[1]+i[2] == v {
            return true
        }
    }
    return false
}
```