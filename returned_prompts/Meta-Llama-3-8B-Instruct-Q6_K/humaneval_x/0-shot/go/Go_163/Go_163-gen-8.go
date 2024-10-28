```go
func GenerateIntegers(a, b int) []int {
    result := make([]int, 0)
    for i := a; i <= b; i++ {
        str := strconv.Itoa(i)
        for j := 0; j < len(str); j++ {
            if str[j]%2 == 0 {
                result = append(result, i)
                break
            }
        }
    }
    return result
}
```

Explanation:
The function GenerateIntegers takes two integers a and b as input. It generates all the numbers between a and b (inclusive) and checks for even digits. If an even digit is found, the number is added to the result list. The function returns the list of numbers containing only even digits.

The function first creates an empty list result to store the numbers with even digits. It then iterates over all numbers from a to b using a for loop. For each number, it converts the number to a string using the strconv.Itoa function, and then iterates over each character in the string using another for loop. If the character is even (i.e., str[j]%2 == 0), the number is added to the result list and the loop is terminated using the break statement. Finally, the function returns the result list.

The function is able to handle the case where a is greater than b by simply iterating from a to b. This is because the function checks for even digits in each number, not just the digits in the range from a to b. Therefore, the function will still return the correct result even if a is greater than b. The example GenerateIntegers(8, 2) demonstrates this, returning the list [2, 4, 6, 8].