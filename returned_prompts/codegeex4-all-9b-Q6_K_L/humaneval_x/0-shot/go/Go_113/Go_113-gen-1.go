Here is the solution:

```go
func OddCount(lst []string) []string {
    result := make([]string, len(lst))
    for i, s := range lst {
        oddCount := 0
        for _, c := range s {
            if c%2 == 1 {
                oddCount++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", oddCount, oddCount, i+1, oddCount)
    }
    return result
}
```

This solution iterates through each string in the input list and counts the number of odd digits. It then uses the `fmt.Sprintf` function to format the output string, replacing the placeholders with the count of odd digits and the index of the string in the input list. The formatted string is then added to the result list, which is returned at the end.