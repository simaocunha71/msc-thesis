
// Convert input hexadecimal string to decimal
hexToDec := func(str string) int {
    dec := 0
    for _, r := range str {
        dec = dec*16 + int(r-'0')
    }
    return dec
}

// Check whether a number is prime or not
prime := func(n int) bool {
    if n == 2 || n == 3 {
        return true
    }
    if n < 2 || n%2 == 0 {
        return false
    }
    for i := 3; i*i <= n; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}

return len(num) - len(strings.ReplaceAll(num, "0", "")) +
    len(num) - len(strings.ReplaceAll(num, "4", "")) +
    len(num) - len(strings.ReplaceAll(num, "6", "")) +
    len(num) - len(strings.ReplaceAll(num, "8", "")) +
    len(num) - len(strings.ReplaceAll(num, "C", "")) +
    len(num) - len(strings.ReplaceAll(num, "9", ""))
}

func HexKey(num string) int {
    hexToDec := func(str string) int {
        dec := 0
        for _, r := range str {
            dec = dec*16 + int(r-'0')
        }
        return dec
    }

    prime := func(n int) bool {
        if n == 2 || n == 3 {
            return true
        }
        if n < 2 || n%2 == 0 {
            return false
        }
        for i := 3; i*i <= n; i += 2 {
            if n%i == 0 {
                return false
            }
        }
        return true
    }

    return len(num) - len(strings.ReplaceAll(num, "0", "")) +
        len(num) - len(strings.ReplaceAll(num,