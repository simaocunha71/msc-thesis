Here is the solution in Go:
```go
func ByLength(arr []int) []string {
    var result []string
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            result = append(result, names[num-1])
        }
    }
    sort.Ints(result)
    reverse(result)
    return result
}

func reverse(arr []string) {
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
}

var names = [...]string{
    "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
}
``` 
This solution first filters out the numbers between 1 and 9, and then appends their corresponding names to the result slice. Then it sorts the result slice and reverses it. If the array has any numbers outside the range [1, 9], they will be ignored. If the array is empty, the function will return an empty slice. 

The reverse function is a simple implementation of reversing a slice in place. The names array is a predeclared array of string constants for numbers from 0 to 9. 

Note: The result slice is returned as is, so you may need to convert it to a string slice if you want to return it as a slice of strings. You can do this by adding `[]string(result)` at the end of the return statement. However, since the problem statement does not specify the return type, I left it as `[]interface{}`. 

This solution assumes that the input array is non-nil. If the input array can be nil, you should add a check at the beginning of the function to handle this case. 

Also, this solution is case-sensitive, so if you want the names to be in lowercase or title case, you will need to modify the names array accordingly. 

This solution has a time complexity of O(n log n) due to the sorting, where n is the length of the input array. The space complexity is O(n) because we need to store the result slice. 