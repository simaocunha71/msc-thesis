// Solution:
func Solve(s string) string {
    result := ""
    for _, char := range s {
        if char >= 'a' && char <= 'z' {
            result += string(char - 32)
        } else if char >= 'A' && char <= 'Z' {
            result += string(char + 32)
        } else {
            result += string(char)
        }
    }
    return result
}
B:
// Solution:
func Solve(s string) string {
    result := ""
    for _, char := range s {
        if char >= 'a' && char <= 'z' {
            result += string(char - 32)
        } else if char >= 'A' && char <= 'Z' {
            result += string(char + 32)
        } else {
            result = result[:0]
            break
        }
    }
    return result
}
C:
// Solution:
func Solve(s string) string {
    result := ""
    for _, char := range s {
        if char >= 'a' && char <= 'z' {
            result += string(char - 32)
        } else if char >= 'A' && char <= 'Z' {
            result += string(char + 32)
        } else {
            if len(result) > 0 {
                result = reverse(result)
            }
        }
    }
    return result
}
D:
// Solution:
func Solve(s string) string {
    var result bytes.Buffer
    for _, char := range s {
        if char >= 'a' && char <= 'z' {
            result.WriteByte(byte(char - 32))
        } else if char >= 'A' && char <= 'Z' {
            result.WriteByte(byte(char + 32))
        } else {
            result.Reset()
        }
    }
    return result.String()
}
E:
// Solution:
func Solve(s string) string {
    var result bytes.Buffer
    for _, char := range s {
        if char >= 'a' && char <= 'z' {
            result.WriteByte(byte(char - 32))
        } else if char >= 'A' && char <= 'Z' {
            result.WriteByte(byte(char + 32))
        } else {
            result.Reset()
            for i := len(s) - 1; i >= 0; i-- {
                result.WriteByte(byte(s[i]))
            }
        }
    }
    return result.String()
}F:
// Solution:
func Solve(s string) string {
    var