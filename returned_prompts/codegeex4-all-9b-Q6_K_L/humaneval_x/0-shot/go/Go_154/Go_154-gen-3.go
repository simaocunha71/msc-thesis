You can use the following code to solve this problem:

```go
func CycpatternCheck(a , b string) bool {
    if len(b) > len(a) {
        return false
    }
    for i := 0; i < len(a); i++ {
        if strings.Contains(a[i:], b) {
            return true
        }
        a = a[1:] + a[:1]
    }
    return false
}
```

Explanation:
- If the length of `b` is greater than `a`, then `b` cannot be a substring of `a`, so return `false`.
- Iterate through `a` and for each position `i`, check if `b` is a substring of `a[i:]`.
- If it is, return `true`.
- If not, rotate `a` by moving the first character to the end and continue the loop.
- If no match is found after all rotations, return `false`.