    if n > m {
        return -1
    } else {
        rounded := math.Round((float64(n) + float64(m)) / 2)
        return fmt.Sprintf("0b%b", int(rounded))
    }
}



