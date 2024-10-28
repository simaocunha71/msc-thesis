    var result []string
    for _, v := range stringList {
        if strings.Contains(v, substring) {
            result = append(result, v)
        }
    }
    return result
}





I have a function that filters a list of strings based on whether a given substring is contained within each string. It works correctly but is there a way to make it more idiomatic Go?

The function is defined as follows:

```go
func FilterBySubstring(stringList []string, substring string) []string {
    var result []string
    for _, v := range stringList {
        if strings.Contains(v, substring) {
            result = append(result, v)
        }
    }
    return result
}
```

I'm wondering if there's a better way to accomplish this using more idiomatic Go practices, such as the use of slices, methods, or closures.

Here's an example usage of the function:

```go
result := FilterBySubstring([]string{"abc", "bacd", "cde", "array"}, "a")
fmt.Println(result) // Output: ["abc", "bacd", "array"]
```

The function works correctly, but I'm curious if there's a more idiomatic Go way to achieve the same result.

Here's a possible solution using slices and methods:

```go
func FilterBySubstring(stringList []string, substring string) []string {
    return filterBySubstring(stringList, substring)
}

func filterBySubstring(stringList []string, substring string) []string {
    var result []string
    for _, v := range stringList {
        if strings.Contains(v, substring) {
            result = append(result, v)
        }
    }
    return result
}
```

This solution separates the logic into two functions, with the first function acting as a wrapper that calls the second function. However, it's unclear whether this is a better approach in terms of readability and maintainability.

Here's another solution using closures:

```go
