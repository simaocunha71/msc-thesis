    var strongest_ext string
    var max_strength float64 = math.MinInt64

    for _, ext := range extensions {
        var strength float64 = 0
        for _, c := range ext {
            if unicode.IsUpper(c) {
                strength++
            } else if unicode.IsLower(c) {
                strength--
            }
        }
        if strength > max_strength {
            max_strength = strength
            strongest_ext = ext
        }
    }
    return class_name + "." + strongest_ext
}
```

### 2. Ticket to Railgun

