import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
// >>> CountDistinctCharacters('xyzXYZ')
// 3
// >>> CountDistinctCharacters('Jerry')
// 4
func CountDistinctCharacters(str string) int{
    var uniqueLetters = make(map[rune]int, 0) // Store all the distinct letters in a map
    for _,r := range str {
        if len(uniqueLetters) == 0 || r != uniqueLetters[r] {
            uniqueLetters[r] += 1
        } else {
            uniqueLetters = map[rune](0:0, 1:1) // Reset the count for distinct letters which occur more than once
        }
    }
    return len(uniqueLetters) // Get number of distinct characters in a string
}

// Given an array of strings, write a function to check if all the strings are
// unique or not
func IsUniqueStrings(arr []string){
    // If length is 1 then it's a no-op check
    if len(arr) == 1 { return }
    for i := 0;i < len(arr);i++{
        if arr[i] != "" && CountDistinctCharacters(arr[i]) > 1 { return false}
    }
    return true // If all string length is more than 1 and unique characters then true, otherwise false
}
// Find the longest common prefix strings in an array of strings
func GetLongestCommonPrefix(arr []string){
    arr = []string{}
    if len(arr) == 0 { return arr }
    var tempArr []string = make([]string, 0) // Store unique values from the original array
    for i := 0;i < len(arr);i++{
        if IsUniqueStrings(arr){
            tempArr = append(tempArr, arr[i])
        }
    }
    return strings.Join(tempArr, "") // Find the longest common prefix string and return it to the caller
}