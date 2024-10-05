    if len(arr) == 0 {
        return nil
    }

    prod := 1
    sum := 0

    for _, v := range arr {
        if v < 0 {
            prod *= -1
        } else if v > 0 {
            prod *= 1
        }
        sum += int(math.Abs(float64(v)))
    }

    return prod * sum
}
```


## 2. Create a function that returns the longest string in an array

