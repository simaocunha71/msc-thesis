    var sum int
    for _, num := range lst {
        if num == float64(int(num)) && num > 0 && num != math.Floor(num) {
            sum += int(math.Pow(num, 2))
        }
    }
    return sum
}
```

### 5. 
