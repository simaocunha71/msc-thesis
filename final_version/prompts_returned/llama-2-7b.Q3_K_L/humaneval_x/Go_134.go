import (
    "strings"
)

// Create a function that returns true if the last character
// of a given string is an alphabetical character and is not
// a part of a word, and false otherwise.
// Note: "word" is a group of characters separated by space.
// 
// Examples:
// CheckIfLastCharIsALetter("apple pie") ➞ false
// CheckIfLastCharIsALetter("apple pi e") ➞ true
// CheckIfLastCharIsALetter("apple pi e ") ➞ false
// CheckIfLastCharIsALetter("") ➞ false
func CheckIfLastCharIsALetter(txt string) bool {
    if strings.HasSuffix(txt, " ") {
        return !CheckWordEndsWithSpace(txt) // if the last character in a string is a space we return false
    } else {
        return (strings.HasSuffix(txt, "a") || strings.HasSuffix(txt, "e")) && CheckNotLastCharIsPartOfABigWord(txt)
    }
}

// Check if the last character is part of a big word
func CheckNotLastCharIsPartOfABigWord(txt string) bool {
    // If len < 1 then we return true because it's just an empty string and there's no possibility to have spaces or other characters in it.
    if len(txt) <= 1 {
        return true
    }
    
    for i := len(txt) - 2; i >= 0; i-- {
        if len(strings.Split(txt, "")) > 1 && strings.HasPrefix(string(txt[i+1:]), " ") {
            return false // we return false because a space character exists before the last character of the string that we are in this function checking for
        }
    }
    
    return true // else the condition is met and therefore all characters are part of a bigger word.
}

// Check if there's any space at the end of an array 
func CheckWordEndsWithSpace(txt string) bool {
    if len(txt) >= 1 && !strings.ContainsAny(string([]rune(txt)[