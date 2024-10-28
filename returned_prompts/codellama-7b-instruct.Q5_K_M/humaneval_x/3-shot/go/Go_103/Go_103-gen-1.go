    if n > m{
        return -1
    }
    sum := 0
    for i := n; i <= m; i++ {
        sum = sum + i
    }
    average := float64(sum) / float64(m-n+1)
    if average == math.Trunc(average) {
        return fmt.Sprintf("%b", int(average))
    }else {
        return fmt.Sprintf("%b", int(math.Round(average)))
    }
}



