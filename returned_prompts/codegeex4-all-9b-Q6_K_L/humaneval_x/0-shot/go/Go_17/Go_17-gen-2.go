func ParseMusic(music_string string) []int{
    var ret []int
    var current int
    var last byte

    for i := 0; i < len(music_string); i++ {
        if music_string[i] == 'o' {
            if last == 'o' {
                ret[current] += 4
            } else {
                current = len(ret)
                ret = append(ret, 4)
            }
            last = 'o'
        } else if music_string[i] == '|' {
            if music_string[i+1] == '.' {
                if last == '|' {
                    ret[current] += 1
                } else {
                    current = len(ret)
                    ret = append(ret, 1)
                }
                last = '|'
                i++
            } else {
                if last == '|' {
                    ret[current] += 2
                } else {
                    current = len(ret)
                    ret = append(ret, 2)
                }
                last = '|'
            }
        }
    }

    return ret
}