```go
func Iscube(a int) bool {
    if a == 0 {
        return true
    }
    root := int(math.Pow(float64(a), 1/3))
    return root*root*root == a
}
```
The `IsCube` function checks if a given integer `a` is the cube of some integer. It first checks if `a` is zero, in which case it returns true because zero is the cube of zero. Then, it calculates the cube root of `a` and checks if the cube of this root is equal to `a`. If it is, then `a` is a cube of some integer and the function returns true. Otherwise, it returns false.