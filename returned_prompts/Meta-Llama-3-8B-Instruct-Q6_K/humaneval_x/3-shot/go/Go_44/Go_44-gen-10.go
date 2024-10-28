    return strconv.FormatInt(int64(x), int(base))
} // or use fmt.Sprintf("%b", x) for binary representation. For other bases use %o for octal and %x for hexadecimal.