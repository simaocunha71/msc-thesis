    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result := ""
    for _, c := range word {
        if !IsVowel(c) {
            continue
        }
        if result != "" {
            return result
        }
        if _, isLeft := leftOf(c, word[len(word)-2]); isLeft {
            result = string(c)
        }
    }
    return result
}

func leftOf(a, b rune) (bool, error) {
    var left, right int
    switch a {
    case 'b', 'c', 'd', 'f', 'g':
        left = index(b)
    case 'a', 'e', 'i', 'o', 'u':
        left = -1
    default:
        return false, errors.New("Invalid input")
    }

    switch b {
    case 'b', 'c', 'd', 'f', 'g':
        right = index(a)
    case 'a', 'e', 'i', 'o', 'u':
        right = -1
    default:
        return false, errors.New("Invalid input")
    }
    return left < right, nil
}

func index(r rune) int {
    var result int
    for i, c := range vowels {
        if c == r {
            result = i
        }
    }
    return result
}

func IsVowel(c rune) bool {
    return len(vowels) > index(c)
}



