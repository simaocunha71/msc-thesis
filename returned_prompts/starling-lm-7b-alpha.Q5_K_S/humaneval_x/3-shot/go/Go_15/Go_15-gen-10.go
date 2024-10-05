    result := strconv.Itoa(n)
    for i:= 1; i <= n; i++ {
        result += " " + strconv.Itoa(i)
    }
    return result
}



