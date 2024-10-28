    // Initialize result
    var count int = 0
    var index int = 0

    // Loop through the string
    for index < len(str) {
        // Check if the characters match
        if str[index:index+len(substring)] == substring {
            // Increase count and check next index
            count++
            index+= len(substring) - 1
        } else {
            index++
        }
    }
    return count
}

// Test cases
fmt.Println(HowManyTimes("", "a"))    // 0
fmt.Println(HowManyTimes("aaa", "a"))  // 3
fmt.Println(HowManyTimes("aaaa", "aa")) // 3
```

Explanation:

This function `HowManyTimes` finds how many times a given substring can be found in the original string. It counts overlapping cases.

The function takes two parameters: `str` (the original string) and `substring` (the substring to be searched).

The function initializes a `count` variable to keep track of the number of times the substring is found in the original string. It also initializes an `index` variable to keep track of the current index in the string.

The function then enters a loop that continues until the `index` is less than the length of the string. Inside the loop, it checks if the characters at the current index in the string match the characters in the substring. If they do, it increments the `count` and updates the `index` to the next index that is `len(substring)` away from the current index. If they don't, it simply increments the `index` to the next character in the string.

Once the loop finishes, the function returns the final count of how many times the substring was found in the original string, including overlapping cases.

The provided test cases demonstrate the usage of the function with different inputs and expected outputs.

```go
func HowManyTimes(str string, substring string) int {
    // Initialize result
    var count int = 0
    var index int = 0

    // Loop through the string
    for index < len(str) {
        // Check if the characters