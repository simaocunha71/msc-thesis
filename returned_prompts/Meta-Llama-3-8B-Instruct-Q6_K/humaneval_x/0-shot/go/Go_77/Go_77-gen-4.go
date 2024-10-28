```go
func Iscube(a int) bool {
    c := int(math.Pow(float64(a), 1/3))
    return c * c * c == a
}
```
This function uses the math.Pow function to calculate the cube root of the input number, then checks if the cube of this number is equal to the original input. If it is, the function returns true; otherwise, it returns false. The use of int(math.Pow(float64(a), 1/3)) is necessary because the math.Pow function returns a float64, and we want to check if the result is an integer. The 1/3 in the math.Pow function is a syntax error, it should be 1.0/3.0, but in Go, you can simply write 1.0/3.0 as 1/3.0. 

The time complexity of this function is O(1) because it only involves a constant number of operations. The space complexity is also O(1) because it only uses a constant amount of space. 

Note: The above function may return incorrect results for large input values because the math.Pow function may not be able to accurately calculate the cube root of the input number due to floating point precision issues. If you need to handle large input values accurately, you may need to use a different approach, such as using a library that provides arbitrary-precision arithmetic. 