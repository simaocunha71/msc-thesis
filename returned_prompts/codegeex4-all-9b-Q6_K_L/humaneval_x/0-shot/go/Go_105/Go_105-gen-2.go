```go
func ByLength(arr []int) []string {
    sort.Ints(arr)
    for i := 0; i < len(arr)/2; i++ {
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    }
    var ret []string
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            ret = append(ret, []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}[num-1])
        }
    }
    return ret
}
```

Explanation:
1. `sort.Ints(arr)` sorts the array in ascending order.
2. The for loop reverses the array.
3. The if statement checks if the number is between 1 and 9 inclusive.
4. If it is, the corresponding name from the array is appended to the result array.
5. The result array is returned.