    binary := strconv.FormatInt(int64(N),2)
    sum := 0
    for _, c := range binary{
        num,_ := strconv.Atoi(string(c))
        sum += num
    }
    return fmt.Sprintf("%d",sum)
}

