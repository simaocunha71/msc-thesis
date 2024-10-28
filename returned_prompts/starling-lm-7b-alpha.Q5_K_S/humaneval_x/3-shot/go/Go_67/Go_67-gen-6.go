    total := 0
    fruit_list := strings.Split(s," and ")
    for _,v := range fruit_list{
        count, _ := strconv.Atoi(v[:len(v)-1])
        total += count
    }
    return n - total
}



