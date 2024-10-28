     count := 0
     vowels := "aeiou"
     s = strings.ToLower(s)

B:
     for _, ch := range s {
         if strings.ContainsRune(vowels, ch) {
             count++
         }
     }

C:
     if len(s) > 0 && s[len(s)-1] == 'y' {
         count++
     }

     return count
}

func main() {
    fmt.Println(VowelsCount("abcde"))
    fmt.Println(VowelsCount("ACEDY"))
}
```

The function `VowelsCount` takes a string `s` as input and converts it to lowercase. Then it iterates over each character in the string. If the character is a vowel, it increments a count. Finally, if the last character of the string is 'y', it increments the count. The function returns the count.

In the main function, we test the `VowelsCount` function with the strings "abcde" and "ACEDY".

This program prints:
```
2
3
```
which are the number of vowels in "abcde" and "ACEDY" respectively.

This is a simple implementation of the problem. However, it assumes that the input string only contains alphabetic characters and is case-insensitive. If there are non-alphabetic characters in the string, the program may not work as expected.

Please note that this program does not handle non-Latin alphabets correctly. For example, it may incorrectly count vowels in strings containing non-Latin alphabets. It also does not handle words with accents or other diacritics. If you need to handle these cases, you will need a more complex solution.

Also, please note that this program only checks for 'y' at the end of the string, but it does not check for 'Y' (capital 'y') at the end of the string. If you need to handle this case, you will need to add a check for 'Y'.

The time complexity of this program is O(n), where n is the length of the string. The space complexity is O(1), as