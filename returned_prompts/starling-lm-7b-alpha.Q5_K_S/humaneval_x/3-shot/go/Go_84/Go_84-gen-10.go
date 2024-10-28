    result := ""
    N_str := strconv.FormatInt(int64(N),2)
    for _,c := range N_str {
        result += string(c)
    }
    return result
}



