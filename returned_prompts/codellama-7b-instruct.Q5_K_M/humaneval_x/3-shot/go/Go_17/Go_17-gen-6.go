    var beats = make([]int,0)

    for _, c := range music_string{
        switch c {
        case 'o':
            beats = append(beats, 4)
        case '|':
            beats = append(beats, 2)
        case '.':
            beats = append(beats, 1)
        }
    }
    return beats
}



