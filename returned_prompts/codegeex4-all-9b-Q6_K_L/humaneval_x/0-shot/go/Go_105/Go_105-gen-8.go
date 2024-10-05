```go
import (
    "sort"
    "strings"
)

// Given an array of integers, sort the integers that are between 1 and 9 inclusive,
// reverse the resulting array, and then replace each digit by its corresponding name from
// "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
//
// For example:
// arr = [2, 1, 1, 4, 5, 8, 2, 3]
// -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8]
// -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
// return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
//
// If the array is empty, return an empty array:
// arr = []
// return []
//
// If the array has any strange number ignore it:
// arr = [1, -1 , 55]
// -> sort arr -> [-1, 1, 55]
// -> reverse arr -> [55, 1, -1]
// return = ['One']
func ByLength(arr []int) []string {
    if len(arr) == 0 {
        return []string{}
    }

    // Filter out numbers not between 1 and 9
    filteredArr := make([]int, 0)
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filteredArr = append(filteredArr, num)
        }
    }

    // Sort and reverse the array
    sort.Ints(filteredArr)
    for i, j := 0, len(filteredArr)-1; i < j; i, j = i+1, j-1 {
        filteredArr[i], filteredArr[j] = filteredArr[j], filteredArr[i]
    }

    // Replace each digit with its corresponding name
    result := make([]string, 0)
    for _, num := range filteredArr {
        result = append(result, map[int]string{
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
           