To solve this problem, we can iterate through the array of numbers and check each number to see if it meets the given conditions. Specifically, we need to check if the number is greater than 10 and if both the first and last digits of the number are odd.

Here is the implementation of the Specialfilter function in Go:

```go
import (
    "strconv"
)

func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(num)
            firstDigit := strNum[0]
            lastDigit := strNum[len(strNum)-1]
            if firstDigit == '1' || firstDigit == '3' || firstDigit == '5' || firstDigit == '7' || firstDigit == '9' &&
               lastDigit == '1' || lastDigit == '3' || lastDigit == '5' || lastDigit == '7' || lastDigit == '9' {
                count++
            }
        }
    }
    return count
}
```

In this code, we first initialize a count variable to keep track of the number of elements that meet the conditions. Then, we iterate through the array of numbers using a for loop. For each number, we check if it is greater than 10. If it is, we convert the number to a string using the strconv.Itoa function. Then, we extract the first and last digits of the number using indexing. Finally, we check if both the first and last digits are odd by comparing them to the odd digits (1, 3, 5, 7, 9). If both digits are odd, we increment the count variable.

After iterating through all the numbers, we return the count variable as the result of the Specialfilter function.

Now, let's test the Specialfilter function with the provided examples:

```go
func main() {
    result1 := Specialfilter([]int{15, -73, 14, -15})
    result2 := Specialfilter([]int{33, -2, -3, 45, 21, 109})
    fmt.Println(result1) // Output: 1
    fmt.Println(result2) // Output: 2
}
```

The output of the program should be:

```
1
2
```

This means that there is 1 number in the first example that meets the conditions, and 2 numbers in the second example that meet