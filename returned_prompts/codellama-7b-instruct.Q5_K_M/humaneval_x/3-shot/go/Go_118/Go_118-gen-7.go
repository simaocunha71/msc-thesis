    var result string

    for i := len(word) - 1; i >= 0; i-- {
        if isVowel(word[i]) {
            if isConsonant(word[i-1]) && isConsonant(word[i+1]) {
                result = word[i:i+1]
                break
            }
        }
    }
    return result
}

func isVowel(c byte) bool {
    return bytes.Equal([]byte{c}, []byte{'a'}) || bytes.Equal([]byte{c}, []byte{'e'}) || bytes.Equal([]byte{c}, []byte{'i'}) || bytes.Equal([]byte{c}, []byte{'o'}) || bytes.Equal([]byte{c}, []byte{'u'})
}

func isConsonant(c byte) bool {
    return !isVowel(c)
}



