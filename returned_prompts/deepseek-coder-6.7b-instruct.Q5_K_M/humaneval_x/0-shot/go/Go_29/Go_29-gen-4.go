
    var output []string

    for _, value := range strings {
        if strings.HasPrefix(value, prefix) {
            output = append(output, value)
        }
    }

    return output

}

```

The function `FilterByPrefix` takes in a list of strings and a prefix string as its arguments. It iterates over each string in the list. If a string starts with the provided prefix, it is added to the output list. Finally, the output list is returned.


## 1.2.2: FilterBySuffix

```go
