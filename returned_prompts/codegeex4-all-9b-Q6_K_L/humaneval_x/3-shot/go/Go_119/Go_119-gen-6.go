    total_left := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                total_left += 1
            } else {
                total_left -= 1
            }
        }
    }

    if total_left == 0 {
        return "Yes"
    } else {
        return "No"
    }
}

