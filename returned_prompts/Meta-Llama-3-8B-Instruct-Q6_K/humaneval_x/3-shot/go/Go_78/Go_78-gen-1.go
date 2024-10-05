    primes := map[rune]bool{'2': true, '3': true, '5': true, '7': true, 'B': true, 'D': true}
    count := 0
    for _, c := range num {
        if _, ok := primes[c]; ok {
            count++
        }
    }
    return count
}  // The map is used to store the hexadecimal digits which are prime numbers. The map key is the hexadecimal digit and the value is true. Then we iterate over the input string, and for each character, we check if it exists in the map. If it does, we increment the count. Finally, we return the count.