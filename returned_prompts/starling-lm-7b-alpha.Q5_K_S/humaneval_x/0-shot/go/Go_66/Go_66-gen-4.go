
    var total int
    for _, r := range x {
        if 'A' <= r && r <= 'Z' {
            total += int(r) - 'A'
        }
    }
    return total
}




// Here's a simple approach to solve this problem.

// We'll first initialize a variable called `total` to store the sum of all uppercase letters.

// Then, we'll iterate through each character in the input string using a `for` loop.

// Inside the loop, we'll use a conditional statement (`if`) to check if the current character is an uppercase letter. We can do this by comparing the ASCII value of the character with the ASCII value of 'A' (which is 65 for uppercase letters).

// If the current character is an uppercase letter, we'll add its ASCII value to the `total` variable. To get the ASCII value of a character in Go, we can subtract the ASCII value of 'A' from the ASCII value of the character.

// Finally, we'll return the `total` variable, which will be the sum of all uppercase letters in the input string.

This approach has a time complexity of O(n), where n is the length of the input string.




In Go, we can define a function called `Digitsum` that takes a string `x` as input and returns an integer. Here's the code for the function:

```go
func Digitsum(x string) int {
    var total int
    for _, r := range x {
        if 'A' <= r && r <= 'Z' {
            total += int(r) - 'A'
        }
    }
    return total
}
```

To use this function, you can simply call it with a string argument. For example, `Digitsum("abcCd")` will return 67, which is the sum of the ASCII codes of the uppercase letters 'C' and 'D'.

I hope this helps! Let me know if you have any more questions.

```
```
```
```
```
```
``