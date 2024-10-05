    result := make([]byte, 0)
    for _, c := range strings.ToUpper(message) {
        if c >= 'A' && c <= 'Z' {
            if c == 'A' {
                result = append(result, 'C')
            } else if c == 'B' {
                result = append(result, 'D')
            } else if c == 'C' {
                result = append(result, 'E')
            } else if c == 'D' {
                result = append(result, 'F')
            } else if c == 'E' {
                result = append(result, 'G')
            } else if c == 'F' {
                result = append(result, 'H')
            } else if c == 'G' {
                result = append(result, 'I')
            } else if c == 'H' {
                result = append(result, 'J')
            } else if c == 'I' {
                result = append(result, 'K')
            } else if c == 'J' {
                result = append(result, 'L')
            } else if c == 'K' {
                result = append(result, 'M')
            } else if c == 'L' {
                result = append(result, 'N')
            } else if c == 'M' {
                result = append(result, 'O')
            } else if c == 'N' {
                result = append(result, 'P')
            } else if c == 'O' {
                result = append(result, 'Q')
            } else if c == 'P' {
                result = append(result, 'R')
            } else if c == 'Q' {
                result = append(result, 'S')
            } else if c == 'R' {
                result = append(result, 'T')
            } else if c == 'S' {
                result = append(result, 'U')
            } else if c == 'T' {
                result = append(result, 'V')
            } else if c == 'U' {
                result = append(result, 'W')
            } else if c == 'V' {
                result = append(result, 'X')
            } else if c == 'W' {
                result = append(result, 'Y')
            } else if c == 'X' {
                result = append(result, 'Z')
            }
        } else {
            result = append(result, c)
        }
    }
    return string(result)
