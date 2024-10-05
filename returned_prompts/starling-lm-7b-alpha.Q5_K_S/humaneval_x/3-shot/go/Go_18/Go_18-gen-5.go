    count := 0
    for startIndex := 0; startIndex < len(str); startIndex++ {
        index := startIndex
        for i := 0; i < len(substring); i++ {
            if index >= len(str) {
                break
            }

            if substring[i] != str[index] {
                break
            }

            index += 1
        }

        if index == len(substring) {
            count += 1
        }
    }

    return count
}



