    count := 0
    for i, v := range s {
        if i%2 == 0 && "ABCDE".contains(string(v)) {
            count++
        }
    }
    return count
}

import (
    "strings"
)

func (s "ABCDE") contains(v string) bool {
    return strings.Contains(s, v)
}

I'm curious if there is a more efficient way to determine if a string is in a fixed set of strings (in this case, the uppercase vowels). 

I was thinking of using a bitset, but it's not very useful since the length of the bitset would be equal to the length of the string to be checked.

I'm not sure if there is a way to do this with a bitset, but it seems like it would be a good idea if there were one.

Here's a possible solution:

func (s "ABCDE") contains(v string) bool {
    return strings.Contains(s, v)
}

func CountUpper(s string) int {
    count := 0
    for i, v := range s {
        if i%2 == 0 && "ABCDE".contains(string(v)) {
            count++
        }
    }
    return count
}

I'm curious if there is a more efficient way to determine if a string is in a fixed set of strings (in this case, the uppercase vowels). 

I was thinking of using a bitset, but it's not very useful since the length of the bitset would be equal to the length of the string to be checked.

I'm not sure if there is a way to do this with a bitset, but it seems like it would be a good idea if there were one.

Here's a possible solution:

func (s "ABCDE") contains(v string) bool {
    return strings.Contains(s, v)
}

func CountUpper(s string) int {
    count := 0
    for i, v := range s {
        if i%2 == 0 && "ABCDE".contains(string(v)) {
            count++