```go
func ByLength(arr []int)[]string {
    // Step 1: Filter out the numbers between 1 and 9
    filtered := []int{}
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }
    
    // Step 2: Sort the filtered array
    sort.Ints(filtered)
    
    // Step 3: Reverse the sorted array
    reversed := make([]int, len(filtered))
    for i, num := range filtered {
        reversed[len(filtered)-1-i] = num
    }
    
    // Step 4: Replace each digit by its corresponding name
    names := []string{}
    for _, num := range reversed {
        names = append(names, numberToWord[num])
    }
    
    return names
}
```

This solution filters out the numbers between 1 and 9, sorts them, reverses the sorted array, and then replaces each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine". If the array has any strange number, it ignores it. If the array is empty, it returns an empty array.