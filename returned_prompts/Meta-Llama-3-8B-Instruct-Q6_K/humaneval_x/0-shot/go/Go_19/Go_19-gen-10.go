Here is a simple and efficient solution in Go. We will split the input string into a slice of strings, sort the slice, and then join the sorted slice back into a string.

```go
import (
    "sort"
    "strings"
)

func SortNumbers(numbers string) string {
    // Split the input string into a slice of strings
    nums := strings.Split(numbers, " ")
    // Sort the slice
    sort.Strings(nums)
    // Join the sorted slice back into a string
    return strings.Join(nums, " ")
}
```

For example, if we call `SortNumbers('three one five')`, it will return `'five one three'`. Note that the sorting is case-insensitive, so 'One' and 'one' will be considered equal. If you want case-sensitive sorting, you can use `sort.SliceStable` instead of `sort.Strings`. 

Also, note that this function assumes that the input string is a space-delimited string of numbers from 'zero' to 'nine'. If the input string can contain other characters or invalid numbers, you may need to add error checking code to handle these cases. 

Finally, this function returns the numbers in the sorted order, but it doesn't remove the 'zero' to 'nine' strings. If you want to remove these strings, you can use a loop to iterate over the sorted slice and remove the strings that are not in the range 'zero' to 'nine'. However, this would require a more complex solution. 

Here is the complete code with error checking:

```go
import (
    "sort"
    "strings"
)

func SortNumbers(numbers string) string {
    // Split the input string into a slice of strings
    nums := strings.Split(numbers, " ")
    // Check if all numbers are valid
    for _, num := range nums {
        if num != "zero" && num != "one" && num != "two" && num != "three" && num != "four" && num != "five" && num != "six" && num != "seven" && num != "eight" && num != "nine" {
            return "Invalid input. Only 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' are allowed."
        }
    }
    // Sort the slice
    sort.Strings(nums)
    // Join the sorted slice back into a string
    return strings.Join(nums,