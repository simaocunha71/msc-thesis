    current_depth := 0
    for _, c := range s {
        if c == '[' {
            current_depth += 1
        }else if c == ']'{
            current_depth -= 1
        }
        if current_depth < 0 {
            return true
        }
    }
    return current_depth > 0
}



