    if n>m {
        return -1
    }
    var sum int = 0
    for i:=n; i<=m; i++ {
        sum += i
    }
    var average float64 = float64(sum)/float64(m-n+1)
    var rounded_average int = int(math.Round(average))
    var binary_average string = fmt.Sprintf("%b", rounded_average)
    return binary_average
}



