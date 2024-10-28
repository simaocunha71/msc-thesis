```go
func FilterBySubstring(stringList []string, substring string) []string {
    result := make([]string, 0)
    for _, s := range stringList {
        if strings.Contains(s, substring) {
            result = append(result, s)
        }
    }
    return result
}
```


Explanation:
This function takes a list of strings and a substring as input. It then iterates over the list of strings and checks if each string contains the given substring using the `strings.Contains` function. If a string contains the substring, it is added to the result list. The function finally returns the result list.

Example usage:
```go
stringsList := []string{"abc", "bacd", "cde", "array"}
result := FilterBySubstring(stringsList, "a")
fmt.Println(result) // Output: ["abc", "bacd", "array"]
```


Note: In this solution, we create a new slice `result` to store the filtered strings. We then iterate over the input slice `stringList` using a range loop. For each string `s` in the input list, we check if it contains the given substring using `strings.Contains`. If it does, we append it to the `result` slice. Finally, we return the `result` slice. This approach is efficient and easy to understand.