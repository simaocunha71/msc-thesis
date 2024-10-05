    count := 0
    for _, v := range arr {
        if strconv.Itoa(v)[0] == "-" {
            count++
        }else{
            if strconv.Itoa(v)[0] == "+" {
                count++
            }else{
                if (strconv.Itoa(v)[0] == "0" && strconv.Itoa(v)[1] == "-") {
                    count++
                }else{
                    if (strconv.Itoa(v)[0] == "0" && strconv.Itoa(v)[1] == "+") {
                        count++
                    }else{
                        if (strconv.Itoa(v)[0] == "0" && strconv.Itoa(v)[1] == "0") {
                            count++
                        }else{
                            count++
                        }
                    }
                }
            }
        }
    }
    return count
}



