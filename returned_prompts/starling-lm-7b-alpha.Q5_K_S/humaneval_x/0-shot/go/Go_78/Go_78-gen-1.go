
    var count int
    for _, r := range num {
        switch {
        case r >= '2' && r <= '3':
            count++
        case r >= '5' && r <= '7':
            count++
        case r >= 'B' && r <= 'D':
            count++
        case r >= 'A' && r <= 'F':
            if r == 'A' {
                if 11%2 == 1 {
                    count++
                }
            } else if r == 'B' {
                if 11%3 == 1 {
                    count++
                }
            } else if r == 'C' {
                if 11%5 == 1 {
                    count++
                }
            } else if r == 'D' {
                if 11%7 == 1 {
                    count++
                }
            } else if r == 'E' {
                if 11%11 == 1 {
                    count++
                }
            } else if r == 'F' {
                if 11%13 == 1 {
                    count++
                }
            }
        }
    }
    return count
}

// HexKey("AB") == 1
// HexKey("1077E") == 2
// HexKey("ABED1A33") == 4
// HexKey("123456789ABCDEF0") == 6
// HexKey("2020") == 2




































































































































