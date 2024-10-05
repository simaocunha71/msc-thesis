    for i, c := range paren_string {
        if c == '(' {
            depth++
        } else if c == ')' {
            depth--
        }
        if depth < 0 {
            break A
        }
    }
    return []int{depth}
}

// 
// 
// 
// 
// 
