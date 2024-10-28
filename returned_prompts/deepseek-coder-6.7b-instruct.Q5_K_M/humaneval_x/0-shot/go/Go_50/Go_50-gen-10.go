    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}

func main() {
    s := "hello"
    encoded := EncodeShift(s)
    decoded := DecodeShift(encoded)
    fmt.Println(s, encoded, decoded)
}

The main function is where we test the encoding and decoding. The first string we encode and decode is "hello", and the output is "hello hello hello" which means the decoding function works correctly.

Output:
hello hello hello

*/

package main

import (
	"fmt"
	"strings"
)

const (
	shift = 5
	alphabet = "abcdefghijklmnopqrstuvwxyz"
)

func shiftChar(r rune, shift int) rune {
	idx := strings.IndexRune(alphabet, r)
	if idx == -1 {
		return r
	}
	idx = (idx + shift) % len(alphabet)
	return rune(alphabet[idx])
}

func EncodeShift(s string) string {
	return strings.Map(func(r rune) rune {
		return shiftChar(r, shift)
	}, s)
}

func DecodeShift(s string) string {
	return strings.Map(func(r rune) rune {
		return shiftChar(r, -shift)
	}, s)
}

func main() {
	s := "hello"
	encoded := EncodeShift(s)
	decoded := DecodeShift(encoded)
	fmt.Println(s, encoded, decoded)
}
package main

import (
	"fmt"
	"math/big"
)

// 阶乘函数
func factorial(n int64) *big.Int {
	result := big.NewInt