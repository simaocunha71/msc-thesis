    result := 0
    str_N := strconv.Itoa(N)
    for _, c := range str_N {
        num, _ := strconv.Atoi(string(c))
        result += num
    }
    result_binary := strconv.FormatInt(int64(result), 2)
    return result_binary
}



