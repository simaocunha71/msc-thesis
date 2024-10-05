    var binary = strconv.FormatInt(int64(N),2)
    var sum int = 0
    for _, i := range binary {
        digit,_ := strconv.Atoi(string(i))
        sum += digit
    }
    return fmt.Sprint(sum)
}

