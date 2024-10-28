Here is a possible solution:
```go
func SortEven(l []int) []int {
    var result []int
    for i, v := range l {
        if i%2 == 0 {
            // even index, sort the values
            sorted := sort.Ints(l[i:i+1])
            result = append(result, sorted[0])
        } else {
            // odd index, keep the value as is
            result = append(result, v)
        }
    }
    return result
}
```
Here's an explanation of the code:

* We create a new slice `result` to store the resulting values.
* We iterate over the input slice `l` using a range loop.
* For each element, we check if the index is even (using the modulo operator `%2 == 0`).
* If the index is even, we sort the values in that index using the `sort.Ints` function, and append the sorted value to the `result` slice.
* If the index is odd, we simply append the original value to the `result` slice.
* Finally, we return the `result` slice.

You can test this function with the examples you provided:
```go
fmt.Println(SortEven([]int{1, 2, 3})) // [1, 2, 3]
fmt.Println(SortEven([]int{5, 6, 3, 4})) // [3, 6, 5, 4]
```I hope this helps! Let me know if you have any questions.