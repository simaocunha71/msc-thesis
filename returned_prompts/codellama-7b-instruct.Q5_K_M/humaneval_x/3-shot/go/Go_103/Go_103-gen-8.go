    if n > m{
        return -1
    }
    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := float64(sum) / float64(m-n+1)
    if avg >= 0 {
        return fmt.Sprintf("0b%b", int(math.Round(avg)))
    }else{
        return -1
    }

}



