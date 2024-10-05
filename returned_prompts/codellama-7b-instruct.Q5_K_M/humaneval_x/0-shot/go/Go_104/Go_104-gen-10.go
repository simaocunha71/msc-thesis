    for i := range x {
        if x[i] < 0 {
            continue A
        }
        if x[i] == 0 {
            continue A
        }
        if x[i]%2 == 0 {
            continue A
        }
        x[i] = strconv.Itoa(x[i])
        sort.Strings(x)
        return x
    }
    return []int{}
}
