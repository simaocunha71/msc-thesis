You can solve this problem by iterating over each character in the string, checking if it is uppercase, and if so, adding its ASCII value to a running total.

Here is a possible solution:

```go
func Digitsum(x string) int {
    sum := 0
    for _, c := range x {
        if c >= 'A' && c <= 'Z' {
            sum += int(c)
        }
    }
    return sum
}
```

Explanation:
- We initialize a variable `sum` to keep track of the running total.
- We iterate over each character `c` in the string `x` using a range loop.
- For each character, we check if it is an uppercase letter by comparing its ASCII value to the ASCII values of 'A' and 'Z'.
- If the character is uppercase, we add its ASCII value to `sum`.
- After the loop, we return `sum` as the result.