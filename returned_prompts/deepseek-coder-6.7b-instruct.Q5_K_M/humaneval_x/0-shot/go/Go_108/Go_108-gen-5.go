    count := 0

    for _, number := range arr {
        sum := 0
        strNum := strconv.Itoa(int(math.Abs(float64(number))))

        for _, char := range strNum {
            digit, _ := strconv.Atoi(string(char))
            sum += digit
        }

        if sum > 0 {
            count++
        }
    }

    return count
}
```


## 3. Fibonacci sequence

