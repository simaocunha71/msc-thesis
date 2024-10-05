    var max string
    for _, w := range words {
        if len(uniqueCharacters(w)) > len(uniqueCharacters(max)) {
            max = w
        } else if len(uniqueCharacters(w)) == len(uniqueCharacters(max)) && lexicographicallyFirst(w, max) {
            max = w
        }
    }
    return max
}

func uniqueCharacters(s string) map[rune]struct{} {
    m := map[rune]struct{}{}
    for _, c := range s {
        m[c] = struct{}{}
    }
    return m
}

func lexicographicallyFirst(a, b string) bool {
    sa := []rune(a)
    sb := []rune(b)
    for i, v := range sa {
        if i >= len(sb) {
            return true
        }
        if v < sb[i] {
            return true
        } else if v > sb[i] {
            return false
        }
    }
    return false
}

I'm not sure if this implementation is correct. It looks fine to me, but it has been failing on one of the tests. The test is:

FindMax(["name", "enam", "game"]) == "enam"

The function returns "game".

It's possible that the test is wrong, but I'd like to verify this first.

Also, is there a more idiomatic way to write the "uniqueCharacters" function?

Here's a sample test code:

package main

import (
    "testing"
)

func TestFindMax(t *testing.T) {
    tests := []struct {
        in  []string
        out string
    }{
        {[]string{"name", "of", "string"}, "string"},
        {[]string{"name", "enam", "game"}, "enam"},
        {[]string{"aaaaaaa", "bb", "cc"}, "aaaaaaa"},
    }

    for _, test := range tests {
        if got := FindMax(test.in); got != test.out {
            t.Errorf