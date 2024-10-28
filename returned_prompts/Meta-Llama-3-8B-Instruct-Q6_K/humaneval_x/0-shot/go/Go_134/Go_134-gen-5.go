Here is a possible solution:
```go
import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Split the string into words
    words := strings.Split(txt, " ")

    // Get the last word
    lastWord := words[len(words)-1]

    // Get the last character of the last word
    lastChar := lastWord[len(lastWord)-1]

    // Check if the last character is an alphabetical character and is not part of a word
    return strings.IsLetter(lastChar) && len(lastWord) > 1 && lastWord[len(lastWord)-2] == ' '
}
```
Here's an explanation of the code:

1. We split the input string into words using the `strings.Split` function.
2. We get the last word from the slice of words.
3. We get the last character of the last word using slicing.
4. We check if the last character is an alphabetical character using the `strings.IsLetter` function.
5. We also check if the last character is not part of a word by checking if the length of the last word is greater than 1 and the character before the last character is a space.

Note that this solution assumes that a "word" is a group of characters separated by space, as mentioned in the problem statement. If the definition of a "word" is different, the solution may need to be modified accordingly.