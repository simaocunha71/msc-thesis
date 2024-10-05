    if n <= 3 {
        switch n {
        case 0:
            return 0
        case 1:
            return 0
        case 2:
            return 2
        case 3:
            return 0
        }
    }
    first, second, third, fourth := 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        first, second, third, fourth = second, third, fourth, first+second+third
    }
    return fourth
}