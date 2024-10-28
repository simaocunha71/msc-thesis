    if n>m {return -1}
    var sum int = 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := float64(sum) / float64(m-n+1)
    if math.Mod(avg,1) < 0.5 {
        return fmt.Sprintf("0b%d", int(avg))
    }else{
        return fmt.Sprintf("0b%d", int(avg+1))
    }
}




