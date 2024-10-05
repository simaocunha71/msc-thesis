    result := 0
    for _, num := range nums {
        s := strconv.Itoa(num)
        if s[0] % 2 != 0 && s[len(s)-1] % 2 != 0 && num > 10 {
            result += 1
        }
    }
    return result
}



