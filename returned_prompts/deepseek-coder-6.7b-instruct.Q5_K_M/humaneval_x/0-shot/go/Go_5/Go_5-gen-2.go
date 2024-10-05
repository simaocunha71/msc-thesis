
    result := make([]int, 0, len(numbers)*2-1)
    for i, num := range numbers {
        result = append(result, num)
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}

```


## 4. Split into Words

Write a function `SplitIntoWords` that takes a string as an argument and returns a list of words in the string. Assume that words are always separated by a single space.

```go
