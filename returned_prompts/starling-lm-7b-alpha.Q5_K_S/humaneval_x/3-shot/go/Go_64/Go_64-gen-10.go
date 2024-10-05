    vowels := map[rune]bool{
        'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'y': true,
    }
    count := 0
    for _, r := range s {
        if vowels[r] {
            count++
        }
    }
    return count
}



