    result := 0
    for i := 0; i < len(strconv.Itoa(n)); i++ {
        if i%2 == 1 {
            result += int(strconv.Itoa(n)[i] - '0')
        }
    }
    return result
}



