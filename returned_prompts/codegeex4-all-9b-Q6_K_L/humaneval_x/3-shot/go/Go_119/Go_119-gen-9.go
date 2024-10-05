    var count int = 0

    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                count += 1
            } else {
                count -= 1
            }
        }
    }

    if count == 0 {
        return "Yes"
    } else {
        return "No"
    }
}



