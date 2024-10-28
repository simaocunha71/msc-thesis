    count := 0
    for _, num := range nums {
        if num > 10 {
            s := strconv.Itoa(num)
            if len(s) >= 2 {
                if s[0] == "1" || s[0] == "3" || s[0] == "5" || s[0] == "7" || s[0] == "9" {
                    if s[len(s)-1] == "1" || s[len(s)-1] == "3" || s[len(s)-1] == "5" || s[len(s)-1] == "7" || s[len(s)-1] == "9" {
                        count += 1
                    }
                }
            }
        }
    }
    return count
}



