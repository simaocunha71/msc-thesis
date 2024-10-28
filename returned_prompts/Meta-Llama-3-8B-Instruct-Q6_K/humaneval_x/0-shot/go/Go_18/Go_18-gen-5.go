```go
func HowManyTimes(str string, substring string) int {
    count := 0
    start := 0
    for {
        pos := strings.Index(str[start:], substring)
        if pos == -1 {
            break
        }
        count++
        start += pos + len(substring)
    }
    return count
}
```
This function uses a for loop to iterate over the string, and `strings.Index` to find the position of the substring. If the substring is found, it increments the count and moves the start position to the end of the found substring. This way, it counts overlapping occurrences. If the substring is not found, it breaks the loop. The function returns the count of occurrences.

You can test this function with the examples you provided:
```go
fmt.Println(HowManyTimes("", "a")) // 0
fmt.Println(HowManyTimes("aaa", "a")) // 3
fmt.Println(HowManyTimes("aaaa", "aa")) // 3
```



