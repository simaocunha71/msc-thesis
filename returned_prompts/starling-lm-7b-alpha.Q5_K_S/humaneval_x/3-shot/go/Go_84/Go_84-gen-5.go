    result := ""
    dec := strconv.Itoa(N)
    for _, v := range dec {
        result += strconv.FormatInt(int64(v-'0'), 2)
    }
    return result
}



