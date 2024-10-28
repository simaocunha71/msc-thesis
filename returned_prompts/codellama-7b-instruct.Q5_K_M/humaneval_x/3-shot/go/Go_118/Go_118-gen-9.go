    var vowels = []rune("aeiouAEIOU")
    var consonants = []rune("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz")
    var closest_vowel string
    var is_closest bool
    var last_vowel_index int
    var last_vowel string

    for i, c := range word {
        if bytes.Contains([]byte{byte(c)}, []byte(consonants)) {
            if last_vowel_index != 0 {
                return last_vowel
            }
        }else{
            if bytes.Contains([]byte{byte(c)}, []byte(vowels)){
                last_vowel = string(c)
                last_vowel_index = i
            }
        }
    }

    return closest_vowel
}



