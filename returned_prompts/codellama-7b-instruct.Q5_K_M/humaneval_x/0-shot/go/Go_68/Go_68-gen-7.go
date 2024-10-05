    for i, num := range arr {
        if num%2 == 0 {
            return []int{num, i}
        }
    }
    return []int{}
}
