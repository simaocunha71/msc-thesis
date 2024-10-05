import (
    "fmt"
    "sort"
)

// In this Kata, you have to sort an array of non-negative integers according to
// number of ones in their binary representation in ascending order.
// For similar number of ones, sort based on decimal value.
// 
// It must be implemented like this:
// >>> SortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
// >>> SortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
// >>> SortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
func SortArray(arr []int) []int {

    // I'm going to use a map to keep track of the number of ones in each number.
    // Then I can sort the map by value and then by key.
    oneCount := make(map[int]int)
    for _, num := range arr {
        if num > 0 {
            ones := 0
            for num > 0 {
                num = num / 2
                ones += num % 2
            }
            oneCount[num] = ones
        }
    }
    // Sort the map by value and then by key.
    // I'm using a custom sort function because I want to sort the map by value,
    // then by key.
    type intPair struct {
        key   int
        value int
    }
    pairs := make([]intPair, 0, len(oneCount))
    for key, value := range oneCount {
        pairs = append(pairs, intPair{key, value})
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].value == pairs[j].value {
            return pairs[i].key < pairs[j].key
        }
        return pairs[i].value < pairs[j].value
    })
    // Convert the map to an array, and return it.
    result := make([]int,