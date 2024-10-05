```go
func AddElements(arr []int, k int) int {
    var sum int
    for i, num := range arr[:k] {
        if len(strconv.Itoa(num)) <= 2 {
            sum += num
        }
    }
    return sum
}
```

Explanation:
This function takes an array of integers `arr` and an integer `k` as input. It initializes a variable `sum` to 0. Then, it loops through the first `k` elements of the array using a range loop. For each element, it checks if the length of the string representation of the element (using `strconv.Itoa`) is less than or equal to 2. If it is, it adds the element to the `sum`. Finally, it returns the `sum`.

For example, given the array `arr = [111,21,3,4000,5,6,7,8,9]` and `k = 4`, the function will add the elements 21 and 3 to the `sum` because they have at most two digits. The result is `24`.