Here's the solution. First, we split the string into a slice of words. Then, we iterate over the slice of words and count the occurrence of each letter. We store the counts in a map. Finally, we find the maximum count and return all the letters that have that count.

```go
func Histogram(test string) map[rune]int {
    words := strings.Fields(test)
    counts := make(map[rune]int)
    max := 0
    for _, word := range words {
        for _, c := range word {
            counts[c]++
            if counts[c] > max {
                max = counts[c]
            }
        }
    }
    result := make(map[rune]int)
    for c, count := range counts {
        if count == max {
            result[c] = count
        }
    }
    return result
}
```

Here's how you can use this function:

```go
fmt.Println(Histogram("a b c")) // Output: map[97:1 98:1 99:1]
fmt.Println(Histogram("a b b a")) // Output: map[97:2 98:2]
fmt.Println(Histogram("a b c a b")) // Output: map[97:2 98:2]
fmt.Println(Histogram("b b b b a")) // Output: map[98:4]
fmt.Println(Histogram("")) // Output: map[]
```

The output is as expected.