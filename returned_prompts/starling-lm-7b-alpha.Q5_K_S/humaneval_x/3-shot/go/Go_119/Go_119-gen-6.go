    count_opening_paranthesis := 0
    count_closing_paranthesis := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                count_opening_paranthesis += 1
            } else if c == ')' {
                count_closing_paranthesis += 1
            }
        }
    }
    if count_opening_paranthesis == count_closing_paranthesis {
        return "Yes"
    } else {
        return "No"
    }
}



