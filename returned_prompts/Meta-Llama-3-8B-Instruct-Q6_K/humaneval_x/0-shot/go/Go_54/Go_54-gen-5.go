```go
func SameChars(s0 string, s1 string) bool {
    m0 := make(map[rune]int)
    m1 := make(map[rune]int)
    for _, r := range s0 {
        m0[r]++
    }
    for _, r := range s1 {
        m1[r]++
    }
    return reflect.DeepEqual(m0, m1)
}
```

Explanation:
This function checks if two words have the same characters. It creates two maps (m0 and m1) to store the frequency of each character in the two strings. Then it compares the two maps using the reflect.DeepEqual function, which returns true if the two maps are equal and false otherwise. If the maps are equal, it means that the two strings have the same characters, regardless of their order or frequency.