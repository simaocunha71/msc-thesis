You can solve this problem by using a map to store the frequency of each number in the list. Then, you can iterate through the map to find the greatest integer that has a frequency greater than or equal to its value. If no such value exists, you can return -1.

Here's the implementation in Go:

```go
func Search(lst []int) int {
    // Create a map to store the frequency of each number
    frequency := make(map[int]int)

    // Count the frequency of each number in the list
    for _, num := range lst {
        frequency[num]++
    }

    // Find the greatest integer that has a frequency greater than or equal to its value
    greatestNum := -1
    for num, freq := range frequency {
        if freq >= num && num > greatestNum {
            greatestNum = num
        }
    }

    return greatestNum
}
```

You can test the function with the given examples:

```go
fmt.Println(Search([]int{4, 1, 2, 2, 3, 1})) // Output: 2
fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4})) // Output: 3
fmt.Println(Search([]int{5, 5, 4, 4, 4})) // Output: -1
```