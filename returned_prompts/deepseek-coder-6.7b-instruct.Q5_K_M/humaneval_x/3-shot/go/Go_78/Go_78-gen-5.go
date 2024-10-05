    prime_map := make(map[rune]bool)
    prime_map['2'] = true
    prime_map['3'] = true
    prime_map['5'] = true
    prime_map['7'] = true
    prime_map['B'] = true
    prime_map['D'] = true

    count := 0

    for _, c := range num {
        if _, ok := prime_map[c]; ok {
            count++
        }
    }

    return count
}



