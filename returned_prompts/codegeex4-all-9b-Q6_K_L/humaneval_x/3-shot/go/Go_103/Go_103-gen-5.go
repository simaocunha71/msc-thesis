    if n>m{
        return -1
    }else{
        avg := (n+m)/2
        return fmt.Sprintf("0b%d", int(math.Pow(2, float64(avg))))
    }
}

