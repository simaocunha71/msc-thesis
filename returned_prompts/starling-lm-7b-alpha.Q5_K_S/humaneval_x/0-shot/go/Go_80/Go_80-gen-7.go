To solve this problem, you can follow these steps:

1. Initialize an empty map called distinctLetters with keys as the letters in the string and values as true. This map will keep track of the distinct letters in the string.

2. Iterate through the string with a for loop, starting from index 0 and ending at length(s)-2 (since the last two indices are out of range). For each iteration, consider the three consecutive letters at indices i, i+1, and i+2.

3. Check if all three letters are distinct. You can do this by checking if the substring of the string from index i to index i+3 (inclusive) is present in the map distinctLetters. If it is not present, it means all three letters are distinct. In that case, update the value of the key in distinctLetters to false, so that it is not considered again in the next iteration.

4. If all three letters are not distinct, return false, as the string is not happy.

5. After the for loop, if the length of the string is less than 3, return true, as the string is happy. Otherwise, check if the last two letters of the string are distinct. If they are, return true, as the string is happy. Otherwise, return false, as the string is not happy.

Here's an example implementation of the solution:

```go
func IsHappy(s string) bool {
    distinctLetters := map[string]bool{}

    for i := 0; i < len(s)-2; i++ {
        if _, ok := distinctLetters[s[i : i+3]]; ok {
            return false
        }
        distinctLetters[s[i : i+3]] = false
    }

    if len(s) < 3 {
        return true
    }
    return s[len(s)-2] != s[len(s)-1]
}
```

You can test the function with the provided test cases to verify its correctness:

```go
fmt.Println(IsHappy("a"))       // false
fmt.Println(IsHappy("aa"))      // false
fmt.Println(IsHappy("abcd"))    // true
fmt.