    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result
}  // Remove the last space
return result[:len(result)-1]  // Use this line to remove the last space



