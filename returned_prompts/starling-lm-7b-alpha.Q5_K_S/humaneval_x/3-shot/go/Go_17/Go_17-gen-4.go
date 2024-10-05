    result := make([]int, 0)
    notes := []string{"o", "o|", ".", "o|", "o", "o|", "o", "o|", "o", "o|", "o"}
    lengths := []int{4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4}

    for i, c := range music_string {
        for j, note := range notes {
            if c == note[i] {
                result = append(result, lengths[j])
            }
        }
    }
    return result
}



