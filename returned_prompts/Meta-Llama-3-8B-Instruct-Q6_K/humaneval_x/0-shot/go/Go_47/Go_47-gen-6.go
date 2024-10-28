```go
func Median(l []int) float64 {
    sort.Ints(l)
    n := len(l)
    mid := n / 2
    if n%2 == 0 {
        return float64(l[mid-1] + l[mid]) / 2
    } else {
        return float64(l[mid])
    }
}
```

This function sorts the input list, then calculates the median. If the length of the list is even, the median is the average of the two middle elements. If the length of the list is odd, the median is the middle element. 

The time complexity of this function is O(n log n) due to the sorting operation. The space complexity is O(1) as it only uses a constant amount of space. 

The function can be used with lists of integers as shown in the example. The function will return the median of the list as a float64 value. 

The function can also be used with other types of comparable values, such as float64 or string, as long as they implement the sort.Interface interface. 

Note that the function does not check for empty lists or lists with non-integer values. It is the responsibility of the caller to ensure that the input list is valid. 

Also, the function uses the built-in sort package in Go, which is stable, meaning that equal elements will maintain their original order after sorting. This is important in some applications, but it is not necessary for calculating the median. 

Finally, the function returns the median as a float64 value, even if the input list contains only integers. This is because the median of a list of integers is always an integer, but the median of a list of floats or other comparable values may not be an integer. If you want to return the median as an integer value for lists of integers, you can use the int64 type and cast the result to int64. However, this is not necessary and may cause issues if the input list contains non-integer values. 