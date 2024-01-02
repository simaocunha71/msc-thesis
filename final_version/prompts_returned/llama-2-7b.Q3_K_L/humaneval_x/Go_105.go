import (
    "sort"
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
func ByLength(arr []int)[]string {
    if len(arr) == 0 {
        return []string{}
    } else if len(arr[0]) > 9 || len(arr) < 1 { // If length of the array is not between 1 and 9, it should be ignored.
        return []string{}
    } else {
        reversedArr := sort.Reverse(sort.IntSlice(arr))
        names := make([]string, len(reversedArr))
        
        for i:=0;i<len(names);i++{
            if arr[i]>=1 && arr[i]<=9 {
                names[i] = "One" + strconv.Itoa(arr[i])
            } else if arr[i] == 10 { // If the array length is more than 9, it should be ignored.
                names