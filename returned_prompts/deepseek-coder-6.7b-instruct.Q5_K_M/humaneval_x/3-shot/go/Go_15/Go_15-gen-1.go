    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result[:len(result)-1] // Trim the trailing space
}



