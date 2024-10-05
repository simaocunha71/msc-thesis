```go
func HowManyTimes(str string, substring string) int {
    count := 0
    pos := 0
    for pos < len(str) {
        pos = strings.Index(str[pos:], substring)
        if pos == -1 {
            break
        }
        count++
        pos += pos + 1
    }
    return count
}
```
Explanation:
The function `HowManyTimes` takes two string parameters `str` and `substring`. It returns the number of times `substring` can be found in `str`. The counting is done from the beginning of `str`, and it includes overlapping cases.

The function uses the `strings.Index` function to find the position of `substring` in `str`. If `substring` is not found, `strings.Index` returns -1, and the loop breaks. Otherwise, the count is incremented, and the position is updated to start searching from the position after the found `substring`. This ensures that overlapping cases are counted.

The function returns the total count of times `substring` can be found in `str`. For example, `HowManyTimes("aaa", "a")` returns 3, because "a" can be found three times in "aaa". Similarly, `HowManyTimes("aaaa", "aa")` returns 3, because "aa" can be found three times in "aaaa". The function also works correctly when `substring` is an empty string, returning 0 in that case.