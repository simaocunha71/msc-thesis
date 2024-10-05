    vowels := "aeiouAEIOU"
    for i := len(word) - 1; i > 0; i-- {
        if bytes.IndexByte([]byte(vowels), word[i]) != -1 {
            return string(word[i])
        }
    }
    return ""
}  // Time complexity: O(n) where n is the length of the word.  // Space complexity: O(1) as we are using a constant amount of space.  // This function scans the word from right to left until it finds a vowel. If it doesn't find any vowel, it returns an empty string. It uses the bytes.IndexByte function to find the index of the vowel in the byte slice of the string. The index is then used to get the vowel from the string. The function uses a for loop to scan the word and the bytes.IndexByte function to find the index of the vowel. It then returns the vowel if found or an empty string if not found.