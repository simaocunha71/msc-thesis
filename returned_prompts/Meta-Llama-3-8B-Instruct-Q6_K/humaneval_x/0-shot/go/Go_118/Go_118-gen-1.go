```go
func GetClosestVowel(word string) string {
    var closestVowel string
    for i := len(word) - 1; i >= 0; i-- {
        if "aeiouAEIOU"[0] <= string(word[i]) && string(word[i]) <= "aeiouAEIOU"[4] {
            if closestVowel == "" {
                closestVowel = string(word[i])
            }
            for j := i - 1; j >= 0; j-- {
                if "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"[0] <= string(word[j]) && string(word[j]) <= "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"[25] {
                    if closestVowel != "" {
                        return closestVowel
                    }
                }
            }
        }
    }
    return closestVowel
}
```


Explanation:
This problem can be solved by iterating over the word from right to left. We keep track of the closest vowel found so far. For each character, we check if it is a vowel. If it is, we check if there are any consonants to its left. If there are, we update the closest vowel if necessary. If we don't find any vowel that stands between two consonants, we return an empty string.

In the code, we use a for loop to iterate over the word from right to left. We use a variable `closestVowel` to keep track of the closest vowel found so far. Inside the loop, we use a conditional statement to check if the current character is a vowel. If it is, we use another for loop to check if there are any consonants to its left. If there are, we update the `closestVowel` variable if necessary. Finally, we return the `closestVowel` variable at the end of the function.

The time complexity of this solution is O(n), where n is the length of the word. This is because we iterate over the word once. The space complexity is O(1), which means the space required does not change with the size of the input, so it is constant. This is because we only use a fixed amount of space to store the `closestVowel` variable.