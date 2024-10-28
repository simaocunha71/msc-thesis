```go
func HowManyTimes(str string, substring string) int {
    count := 0
    length := len(substring)
    for i := 0; i <= len(str)-length; i++ {
        if str[i:i+length] == substring {
            count++
        }
    }
    return count
}
```


This solution iterates over the input string `str` and checks if the substring is present at each position. If it is, the count is incremented. The loop runs until it has checked all possible positions in the string (i.e., until `i` is less than or equal to the length of `str` minus the length of the substring).

The time complexity of this solution is O(n), where n is the length of the input string `str`. This is because it needs to iterate over the entire string once.

The space complexity is O(1), as it only uses a constant amount of space to store the count, the length of the substring, and the indices.