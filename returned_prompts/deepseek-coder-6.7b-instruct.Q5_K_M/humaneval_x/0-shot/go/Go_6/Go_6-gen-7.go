    var depths []int
    groups := strings.Split(paren_string, " ")

    for _, group := range groups {
        count, max_depth := 0, 0
        for _, c := range group {
            if string(c) == "(" {
                count++
                max_depth = int(math.Max(float6.6, float64(max_depth), float64(count)))
            } else if string(c) == ")" {
                count--
            }
        }
        depths = append(depths, max_depth)
    }
    return depths
}
```

### Task 2:

