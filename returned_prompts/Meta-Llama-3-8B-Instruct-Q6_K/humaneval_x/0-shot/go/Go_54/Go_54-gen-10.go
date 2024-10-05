```go
func SameChars(s0 string, s1 string) bool {
    // Convert the strings to slices of runes
    runes0 := []rune(s0)
    runes1 := []rune(s1)

    // Sort the slices
    sort.Slice(runes0, func(i, j int) bool { return runes0[i] < runes0[j] })
    sort.Slice(runes1, func(i, j int) bool { return runes1[i] < runes1[j] })

    // Compare the sorted slices
    return reflect.DeepEqual(runes0, runes1)
}
```

Explanation:

The problem is asking to check if two words have the same characters, regardless of their order and frequency. To solve this, we can convert the strings to slices of runes, sort the slices, and then compare them.

Here's how it works:

1. Convert the strings to slices of runes using the `[]rune` syntax. This gives us arrays of Unicode code points.
2. Sort the slices using the `sort.Slice` function. This rearranges the runes in each slice in a specific order (lexicographically).
3. Compare the sorted slices using the `reflect.DeepEqual` function. This checks if the two slices are equal, ignoring the order of the runes.

By sorting the slices, we can ignore the order of the characters in the original strings and focus on their frequency. If two strings have the same characters, their sorted slices will be equal. If they have different characters, their sorted slices will be different.

Note that this solution assumes that the input strings only contain Unicode code points that can be sorted lexicographically. If the input strings contain non-sortable characters (such as non-ASCII characters), this solution may not work correctly. In that case, you would need to use a more advanced sorting algorithm that can handle non-sortable characters.