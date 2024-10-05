    count := 0
    for _, num := range nums{
        if num > 10 && (strconv.Itoa(num)[0] == "1" || strconv.Itoa(num)[0] == "3" || strconv.Itoa(num)[0] == "5" || strconv.Itoa(num)[0] == "7" || strconv.Itoa(num)[0] == "9"){
            count += 1
        }
    }
    return count
}



