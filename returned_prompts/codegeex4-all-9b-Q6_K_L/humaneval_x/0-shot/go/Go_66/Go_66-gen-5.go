package kata

func Digitsum(x string) (res int) {
	for _, c := range x {
		if c >= 'A' && c <= 'Z' {
			res += int(c)
		}
	}
	return
}

func TestDigitsum(t *testing.T) {
	assert.Equal(t, 0, Digitsum(""))
	assert.Equal(t, 131, Digitsum("abAB"))
	assert.Equal(t, 67, Digitsum("abcCd"))
	assert.Equal(t, 69, Digitsum("helloE"))
	assert.Equal(t, 131, Digitsum("woArBld"))
	assert.Equal(t, 153, Digitsum("aAaaaXa"))
}