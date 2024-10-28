
    result := []int{}
    for i, number := range numbers {
        result = append(result, number)
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}
```


## Answer Key
```go
