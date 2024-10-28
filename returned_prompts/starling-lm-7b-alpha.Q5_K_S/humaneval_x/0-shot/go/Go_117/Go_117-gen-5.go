    var buffer bytes.Buffer
    words := strings.Fields(s)
    var result []string
    for _, word := range words {
        count := 0
        for _, rune := range word {
            if !isVowel(rune) {
                count++
            }
            if count == n {
                buffer.WriteString(word + " ")
            }
        }
    }
    result = append(result, buffer.String())
    return result
}

func isVowel(r rune) bool {
    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'y'}
    for _, v := range vowels {
        if v == r {
            return true
        }
    }
    return false
}

/*
Mary had a little lamb
  Mary     1
  had      1
  a        1
  little   3
  lamb     2

Mary had a little lamb
  Mary     1
  had      1
  a        1
  little   3
  lamb     2

simple white space
  simple   2
  white    2
  space    2

Hello world

Uncle sam
  Uncle   3
  sam     2

*/

/*
Mary had a little lamb
  Mary     1
  had      1
  a        1
  little   3
  lamb     2

Mary had a little lamb
  Mary     1
  had      1
  a        1
  little   3
  lamb     2

simple white space
  simple   2
  white    2
  space    2

Hello world

Uncle sam
  Uncle   3
  sam     2

*/

import (
    "bytes"
    "strings"
)

// Given a string s and a natural number n, you have been tasked to implement
// a function that returns a list of all words from string s that contain exactly
// n consonants, in order these words appear in the string s.
// If the string s is empty then the function should return an empty list.
// Note: you may assume the