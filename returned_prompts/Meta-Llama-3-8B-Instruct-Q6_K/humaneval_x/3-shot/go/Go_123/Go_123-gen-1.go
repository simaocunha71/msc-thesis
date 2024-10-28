    var result []int
    for n != 1 {
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
        if n != 1 && !contains(result, n) {
            result = append(result, n)
        }
    }
    result = append(result, 1)
    sort.Ints(result)
    return result
}

func contains(arr []int, target int) bool {
    for _, v := range arr {
        if v == target {
            return true
        }
    }
    return false
}
}