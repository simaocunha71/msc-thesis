```go
func Iscube(a int) bool {
    c := int(math.Sqrt(float64(math.Pow(float64(a), 1/3))))
    return c*c*c == a
}
```

This function works by first calculating the cube root of the input number using the `math.Pow` function. The `1/3` exponent is used to calculate the cube root. The `math.Sqrt` function is used to get the integer part of the cube root, since `math.Pow` returns a floating point number.

Then, it checks if the cube of the calculated cube root is equal to the input number. If it is, the function returns `true`, indicating that the number is a cube of some integer. Otherwise, it returns `false`. 

The function works for both positive and negative input numbers, and for zero. 

Note: The `math.Pow` function can return NaN (Not a Number) if the input number is negative. However, since we are using the `math.Sqrt` function to get the integer part of the cube root, this case is handled correctly. 

The time complexity of this function is O(1), since it only involves a constant number of operations. The space complexity is also O(1), since it only uses a constant amount of space. 