var result int
temp := N
for temp > 0 {
    digit := temp % 2
    result += digit
    temp /= 2
}
return strconv.Itoa(result)
}

