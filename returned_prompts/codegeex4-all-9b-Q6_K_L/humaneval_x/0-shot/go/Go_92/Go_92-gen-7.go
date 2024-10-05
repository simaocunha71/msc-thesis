```go
func AnyInt(x, y, z interface{}) bool {
    xi, yi, zi := x.(int), y.(int), z.(int)
    return xi == yi+zi || yi == xi+zi || zi == xi+yi
}
```