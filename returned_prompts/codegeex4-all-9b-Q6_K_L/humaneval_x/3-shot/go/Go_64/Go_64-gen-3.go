Your implementation of VowelsCount is correct, but it could be more efficient. Instead of using strings.ContainsRune, you can simply convert the string to a slice of runes and then iterate over it. This will give you the same result, but it will be faster.

Here's a more efficient version of your code:

func VowelsCount(s string) int {
    vowels := []rune{'a', 'e', 'i', 'o', 'u'}
    count := 0

    for _, c := range strings.ToLower(s) {
        if c == 'y' && strings.HasSuffix(s, "y") {
            count++
        } else if sliceContainsRune(vowels,