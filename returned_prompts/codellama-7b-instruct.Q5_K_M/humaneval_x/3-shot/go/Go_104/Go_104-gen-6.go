    y := make([]string, len(x))

    for i, v := range x {
        y[i] = strconv.Itoa(v)
    }

    sort.Strings(y)

    z := make([]int, len(y))

    for i, v := range y {
        z[i], _ = strconv.Atoi(v)
    }

    result := make([]int, 0)

    for _, v := range z {
        if v % 2 != 0 {
            result = append(result, v)
        }
    }
    return result
}



