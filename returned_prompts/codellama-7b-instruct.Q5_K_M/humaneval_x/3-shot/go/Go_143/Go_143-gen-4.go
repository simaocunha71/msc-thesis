    var result string = ""

    for _, word := range strings.Split(sentence, " ") {
        if IsPrime(len(word)) {
            result += word + " "
        }
    }

    return strings.TrimSpace(result)
}

func IsPrime(number int) bool {
    if number < 2 {
        return false
    }
    for i := 2; i*i <= number; i++ {
        if number % i == 0 {
            return false
        }
    }
    return true
}



