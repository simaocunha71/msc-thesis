package kata

func Digitsum(x string) int {
    sum := 0
    for _, c := range x {
        if c >= 'A' && c <= 'Z' {
            sum += int(c)
        }
    }
    return sum
}

func TestDigitsum(t *testing.T) {
    assert.Equal(t, 0, Digitsum(""))
    assert.Equal(t, 131, Digitsum("abAB"))
    assert.Equal(t, 67, Digitsum("abcCd"))
    assert.Equal(t, 69, Digitsum("helloE"))
    assert.Equal(t, 131, Digitsum("woArBld"))
    assert.Equal(t, 153, Digitsum("aAaaaXa"))
}