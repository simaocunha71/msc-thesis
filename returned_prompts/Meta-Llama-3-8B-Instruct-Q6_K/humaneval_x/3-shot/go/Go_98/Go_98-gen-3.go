    count := 0
    for i := 0; i < len(s); i++ {
        if i % 2 == 0 && strings.ToUpper(string(s[i])) == string(s[i]) {
            count++
        }
    }
    return count
}  // 0-based indexing, so even indices are 0, 2, 4, etc.  This code counts the number of uppercase vowels at these indices.  The strings.ToUpper function is used to convert the character to uppercase and then compare it with the original string.  If they are equal, the character is an uppercase vowel.  The result is the count of uppercase vowels at even indices.  If you want to count uppercase vowels at odd indices, you can change the condition to i % 2 != 0.  If you want to count uppercase vowels at all indices, you can remove the condition and just count the uppercase vowels.  If you want to count lowercase vowels at even indices, you can change the condition to i % 2 == 0 && strings.ToLower(string(s[i])) == string(s[i]).  If you want to count lowercase vowels at odd indices, you can change the condition to i % 2 != 0 && strings.ToLower(string(s[i])) == string(s[i]).  If you want to count vowels at even indices, you can change the condition to i % 2 == 0 && strings.Contains("aeiouAEIOU", string(s[i])).  If you want to count vowels at odd indices, you can change the condition to i % 2 != 0 && strings.Contains("aeiouAEIOU", string(s[i])).