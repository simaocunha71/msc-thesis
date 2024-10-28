Here is the solution:

```go
func ByLength(arr []int) []string {
    // Filter out the numbers that are between 1 and 9 inclusive
    filtered := []int{}
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }
    
    // Sort the filtered array in ascending order
    sort.Ints(filtered)
    
    // Reverse the sorted array
    for i := 0; i < len(filtered)/2; i++ {
        filtered[i], filtered[len(filtered)-1-i] = filtered[len(filtered)-1-i], filtered[i]
    }
    
    // Replace each digit by its corresponding name
    names := []string{}
    for _, num := range filtered {
        names = append(names, map[int]string{
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }[num])
    }
    
    return names
}
```

This function first filters out the numbers that are between 1 and 9 inclusive, then sorts the filtered array in ascending order, and then reverses the sorted array. Finally, it replaces each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" and returns the resulting array.