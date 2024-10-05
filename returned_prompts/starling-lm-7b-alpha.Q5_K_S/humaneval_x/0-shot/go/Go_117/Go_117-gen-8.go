    var result []string
    var buf bytes.Buffer
    var ok bool
    for _, r := range s {
        if r == ' ' {
            if ok {
                buf.Reset()
            } else {
                continue
            }
            if countVowels(buf.String()) == n {
                result = append(result, buf.String())
            }
            ok = true
            continue
        }
        if !isVowel(r) {
            buf.WriteByte(r)
        } else {
            ok = false
        }
    }
    return result
}

func countVowels(s string) int {
    cnt := 0
    for _, r := range s {
        if r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u' {
            cnt++
        }
    }
    return cnt
}

func isVowel(r rune) bool {
    switch r {
    case 'a', 'e', 'i', 'o', 'u':
        return true
    }
    return false
}

The code is in Go language, which is a statically typed language.

In the function SelectWords, the parameter s is a string, and the parameter n is an integer. The function returns a slice of strings.

The function first initializes an empty result slice, a bytes.Buffer object called buf, and a boolean variable ok.

Next, it iterates over each rune (unicode code point) in the input string s. If the rune is a space, it checks the value of ok: if ok is true, it resets the buf and continues; otherwise, it continues the loop. If the rune is not a vowel, it writes the rune to the buf; otherwise, it sets ok to false.

After the loop, the function checks if ok is true. If so, it checks if the count of vowels in buf is equal to n. If they are equal, it appends buf to the result slice.

Finally, the function returns the result slice.

The function countVowels takes a string as input and returns the number of vowels in