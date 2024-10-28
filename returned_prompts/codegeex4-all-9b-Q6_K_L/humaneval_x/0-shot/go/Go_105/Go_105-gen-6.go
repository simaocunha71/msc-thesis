package main

import (
    "sort"
    "fmt"
)

var numberNames = []string{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}

func ByLength(arr []int) []string {
    if len(arr) == 0 {
        return []string{}
    }
    var filteredArr []int
    for _, val := range arr {
        if val > 0 && val <= 9 {
            filteredArr = append(filteredArr, val)
        }
    }
    sort.Ints(filteredArr)
    reversedArr := reverseArr(filteredArr)
    return convertToNames(reversedArr)
}

func reverseArr(arr []int) []int {
    var reversedArr []int
    for i := len(arr) - 1; i >= 0; i-- {
        reversedArr = append(reversedArr, arr[i])
    }
    return reversedArr
}

func convertToNames(arr []int) []string {
    var names []string
    for _, val := range arr {
        names = append(names, numberNames[val])
    }
    return names
}

func main() {
    arr := []int{2, 1, 1, 4, 5, 8, 2, 3}
    fmt.Println(ByLength(arr))
}