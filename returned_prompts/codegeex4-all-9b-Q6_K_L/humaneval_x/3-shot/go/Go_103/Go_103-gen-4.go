    if n > m{
        return -1
    }else{
        return fmt.Sprintf("0b%b",int(math.Round(float64(n+m)/2)))
    }
}



