    for _, num := range x {
        if strconv.Itoa(num)[0]%2 == 0 {
            x = append(x, num)
        }
    }

    sort.Ints(x)

    return x
}
