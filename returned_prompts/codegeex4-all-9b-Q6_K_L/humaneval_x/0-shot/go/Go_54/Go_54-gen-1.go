Here is the solution in Go:

```go
func SameChars(s0 string, s1 string) bool {
    // create a slice of runes from the strings
    runes0 := []rune(s0)
    runes1 := []rune(s1)

    // check if the lengths of the slices are equal
    if len(runes0) != len(runes1) {
        return false
    }

    // create a map to store the count of each rune in s0
    runeCount := make(map[rune]int)
    for _, r := range runes0 {
        runeCount[r]++
    }

    // check if each rune in s1 is in s0 and has the same count
    for _, r := range runes1 {
        if runeCount[r] == 0 {
            return false
        }
        runeCount[r]--
    }

    return true
}
```

This function first converts the strings into slices of runes. It then checks if the lengths of the slices are equal. If not, it returns false.

Next, it creates a map to store the count of each rune in the first slice. It then iterates over the second slice and checks if each rune is in the map and has a count greater than 0. If not, it returns false.

If all checks pass, it returns true.

I hope this helps! Let me know if you have any questions.