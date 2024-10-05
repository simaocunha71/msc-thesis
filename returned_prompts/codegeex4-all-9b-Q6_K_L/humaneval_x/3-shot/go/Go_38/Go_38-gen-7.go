    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append(runes[2:], runes[0], runes[1])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

// Takes as input string, and encodes it twice. Then decodes it once.
// Return the final decoded string.
func EncodeDecode(s string) string {
    return DecodeCyclic(EncodeCyclic(EncodeCyclic(s)))
}

// Takes as input string, and encodes it twice. Then decodes it twice.
// Return the final decoded string.
func DecodeEncode(s string) string {
    return EncodeCyclic(DecodeCyclic(DecodeCyclic(s)))
}

// Takes as input string, and encodes it three times. Then decodes it twice.
// Return the final decoded string.
func EncodeDecodeEncode(s string) string {
    return DecodeCyclic(EncodeCyclic(DecodeCyclic(EncodeCyclic(s))))
}

// Takes as input string, and encodes it three times. Then decodes it three times.
// Return the final decoded string.
func DecodeEncodeEncode(s string) string {
    return EncodeCyclic(DecodeCyclic(DecodeCyclic(DecodeCyclic(s))))
}

// Takes as input string, and encodes it four times. Then decodes it twice.
// Return the final decoded string.
func EncodeEncodeDecode(s string) string {
    return DecodeCyclic(EncodeCyclic(EncodeCyclic(DecodeCyclic(s))))
}

// Takes as input string, and encodes it four times. Then decodes it three times.
// Return the final decoded string.
func DecodeEncodeEncodeDecode(s string) string {
    return EncodeCyclic(DecodeCyclic(DecodeCyclic(DecodeCyclic(DecodeCyclic(s)))))
}

// Takes as input string, and encodes it five times. Then decodes it twice.
// Return the final decoded string.
func EncodeEncodeEncodeDecode(s string) string {
   