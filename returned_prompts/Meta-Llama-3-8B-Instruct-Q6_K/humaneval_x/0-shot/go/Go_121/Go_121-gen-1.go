
You can use a for loop to iterate over the list of integers. For each element, you can check if its position is even and if it's an odd number. If both conditions are true, you can add the number to the sum.

Here is the code in Go:
```
func Solution(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%2 == 0 && v%2 != 0 {
            sum += v
        }
    }
    return sum
}
```
This code uses the modulo operator (`%`) to check if the position `i` is even (i.e., `i%2 == 0`). It also uses the modulo operator to check if the number `v` is odd (i.e., `v%2 != 0`). If both conditions are true, it adds the number to the sum.

You can test this function with the examples you provided:
```
fmt.Println(Solution([]int{5, 8, 7, 1})) // Output: 12
fmt.Println(Solution([]int{3, 3, 3, 3, 3})) // Output: 9
fmt.Println(Solution([]int{30, 13, 24, 321})) // Output: 0
```