```go
func GetPositive(l []int) []int {
    var result []int
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}
```
Explanation:
The function `GetPositive` takes a slice of integers as input and returns a new slice containing only the positive numbers from the original slice.

The function uses a loop to iterate over each element in the input slice. For each element, it checks if the element is greater than 0 using the conditional statement `if v > 0`. If the element is positive, it is appended to the `result` slice using the `append` function.

Finally, the function returns the `result` slice, which contains only the positive numbers from the original slice. If the input slice is empty, the function returns an empty slice.

The function is efficient and scalable because it uses a simple loop and the `append` function, which has a time complexity of O(1) and O(n) respectively, where n is the length of the input slice. Therefore, the overall time complexity of the function is O(n), where n is the length of the input slice. The space complexity is O(n) because the function creates a new slice to store the result.