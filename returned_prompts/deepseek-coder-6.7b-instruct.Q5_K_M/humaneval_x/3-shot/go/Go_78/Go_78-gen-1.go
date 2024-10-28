    count := 0
    prime := []string{"2", "3", "5", "7", "B", "D"}
    for _, v := range num {
        if strings.Contains(strings.Join(prime, ""), string(v)) {
            count++
        }
    }
    return count
}



