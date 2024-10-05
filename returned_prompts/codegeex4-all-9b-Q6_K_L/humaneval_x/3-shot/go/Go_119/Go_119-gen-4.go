    count := 0

    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                count++
            } else if c == ')' {
                count--
            }
        }
    }

    if count == 0 {
        return "Yes"
    } else {
        return "No"
    }
}

