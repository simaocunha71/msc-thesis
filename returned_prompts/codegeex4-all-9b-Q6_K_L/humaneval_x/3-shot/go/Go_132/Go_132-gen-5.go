    depth := 0
    for _, c := range s{
        if c == '['{
            depth += 1
        }else{
            depth -= 1
        }

        if depth == 0{
            return true
        }
    }
    return false
}

