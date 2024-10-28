    count := 0
    for _, num := range nums {
        num_str := strconv.Itoa(num)
        if num > 10 && ((num_str[0] == "1" || num_str[0] == "3" || num_str[0] == "5" || num_str[0] == "7" || num_str[0] == "9") && (num_str[len(num_str)-1] == "1" || num_str[len(num_str)-1] == "3" || num_str[len(num_str)-1] == "5" || num_str[len(num_str)-1] == "7" || num_str[len(num_str)-1] == "9")) {
            count += 1
        }
    }
    return count
}



