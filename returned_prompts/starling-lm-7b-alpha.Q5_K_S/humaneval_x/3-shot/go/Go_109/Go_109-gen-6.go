    s := make([]int, 0, len(arr))
    for _, v := range arr {
        s = append(s, v)
    }
    sort.Ints(s)

    for i := 0; i < len(s); i++ {
        if s[i] != arr[i] {
            return false
        }
        if i+1 < len(s) && s[i+1] == s[i] {
            return false
        }
    }
    return true
}



