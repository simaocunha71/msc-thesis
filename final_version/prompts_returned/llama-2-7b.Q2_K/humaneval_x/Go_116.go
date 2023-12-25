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
    // In the next line of code, you will sort this array into ascending order.
    // You cannot use any of the usual sorting methods, so you are free to come up with your own.
    // You must return a new copy of the sorted data set.
    bins := make([]int, 0, len(arr))
    for _, v := range arr {
        bins = append(bins, binaryToBits(v, bins)...)
    }
    sort.SliceStable(bins, func(i, j int) bool { return sort.IntsAreLessThan(bins[i], bins[j]) })
    res := make([]int, 0, len(arr))
    for _, v := range arr {
        res = append(res, decimalToBits(v, bins)...)
    }
    return res
}

func binaryToBits(n int, bs []int) []int {
    bits := make([]int, 0, binaryLog10(float64(n)))
    for i := 0; i < len(bits); i += 8 {
        nbins := 7 - (i/8) + 1
        for j := 0; j <= nbins; j++ {
            p1, _ := parsePowerOfTwo(j, true