    return len(q)%2 == 0 && sum(q) <= w
}

func sum(q []int) int {
    result := 0
    for _, v := range q {
        result += v
    }
    return result
}



