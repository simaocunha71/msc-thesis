    for i := range lst {
        if lst[i] < 0 || !math.IsInt(lst[i]) {
            continue A
        }
    }
    sum := 0
    for i := range lst {
        if lst[i]%2 == 0 {
            sum += int(lst[i])
        } else {
            sum += int(lst[i]) * 2
        }
    }
    return sum
}

