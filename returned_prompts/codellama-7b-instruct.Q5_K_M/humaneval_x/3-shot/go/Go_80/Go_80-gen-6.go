    var hashmap = make(map[rune]bool)
    var count = 0
    for _, c := range s {
        if _, ok := hashmap[c]; ok {
            count += 1
        }
        hashmap[c] = true
    }
    return count <= 1
}



