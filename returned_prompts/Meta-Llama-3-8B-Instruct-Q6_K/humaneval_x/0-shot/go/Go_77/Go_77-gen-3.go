```go
func Iscube(a int) bool {
    c := int(math.Ceil(math.Pow(float64(a), (1.0/3.0))))
    for i := c; i >= 1; i-- {
        if math.Pow(float64(i), 3) == float64(a) {
            return true
        }
    }
    return false
}
```

Explanation:
This function checks if the given integer `a` is a perfect cube. A perfect cube is an integer that is the cube of an integer. For example, 1, 8, 27, 64, etc. are all perfect cubes.

The function starts by calculating the ceiling of the cube root of `a`. This is done to ensure that we don't miss any potential cubes. The ceiling of the cube root of `a` is the smallest integer that is greater than or equal to the cube root of `a`.

Then, the function iterates from the ceiling of the cube root of `a` down to 1. For each integer `i` in this range, it checks if `i` cubed is equal to `a`. If it is, the function returns `true`, indicating that `a` is a perfect cube.

If the function iterates through the entire range without finding a match, it returns `false`, indicating that `a` is not a perfect cube.

The time complexity of this function is O(√a), because we are iterating up to the ceiling of the cube root of `a`. The space complexity is O(1), because we are using a constant amount of space to store the variables `c` and `i`.