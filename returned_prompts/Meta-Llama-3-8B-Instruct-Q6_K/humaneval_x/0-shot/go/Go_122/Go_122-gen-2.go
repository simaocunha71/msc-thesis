Here is a simple and efficient solution in Go:
```go
func AddElements(arr []int, k int) int {
    sum := 0
    for i := 0; i < k && i < len(arr); i++ {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}
```
Here's an explanation of the code:

1. We initialize a variable `sum` to 0, which will store the sum of the elements with at most two digits.
2. We loop through the first `k` elements of the array using a for loop.
3. For each element, we convert it to a string using `strconv.Itoa` and check its length. If the length is less than or equal to 2, it means the element has at most two digits, so we add it to the `sum`.
4. We return the final `sum` value.

This solution has a time complexity of O(k) and a space complexity of O(1), making it efficient for large arrays.