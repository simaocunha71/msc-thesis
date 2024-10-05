    return l == monotonically_increasing(l) || l == monotonically_decreasing(l)
}

func monotonically_increasing(l []int) []int {
    for i := 1; i < len(l); i++ {
        if l[i-1] > l[i] {
            return l
        }
    }
    return l
}

func monotonically_decreasing(l []int) []int {
    for i := 1; i < len(l); i++ {
        if l[i-1] < l[i] {
            return l
        }
    }
    return l
}



