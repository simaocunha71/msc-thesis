    var result []string
    for _, word := range strings.Fields(s) {
        var count int
        for _, c := range word {
            if "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" != string(c) + string("абвгдеёжзийклмнопрстуфхцчшщъыьэюя") {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}



