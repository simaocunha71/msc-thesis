```
    i := 0
    count := 0

    for i <= len(str) {
        pos := strings.Index(str[i:], substring)
        if pos == -1 {
            break
        }
        count++
        i += pos + len(substring)
    }
    return count
}
```
In the above code, we are iterating over the original string `str` and for each position, we are searching for the `substring` using `strings.Index()`. If the `substring` is found, we increment the `count` and move the current position to the end of the `substring` plus one. This ensures that we don't count the same occurrence of the `substring` multiple times. We break the loop when we no longer find the `substring` in the remaining part of the `str`. The `count` variable will hold the number of times the `substring` appears in the `str`. This function will return the count of overlapping matches. If you want to avoid overlapping matches, you can modify the code to `i += len(substring)`. This will move the current position to the end of the `substring` without considering the overlapping matches. 

For example, if the `str` is `'aaa'` and `substring` is `'a'`, the function will return `3` without overlapping matches, but if you want to count overlapping matches, it will return `4`. 

Here is the modified code for non-overlapping matches:

```go
func HowManyTimes(str string, substring string) int {
    i := 0
    count := 0

    for i <= len(str) {
        pos := strings.Index(str[i:], substring)
        if pos == -1 {
            break
        }
        count++
        i += pos + len(substring)
    }
    return count
}
```

And here is the modified code for overlapping matches:

```go
func HowManyTimes(str string, substring string) int {
    i := 0
    count := 0

    for i <= len(str) {
        pos := strings.Index(str[i:], substring)
        if pos == -1 {
            break
        }
        count++
        i += len(substring)
    }
    return count
}
```


Please note that the function `HowManyTimes` will return `0` if the `substring` is an empty string or if the `str` is an empty string. This is because an empty string is considered as a