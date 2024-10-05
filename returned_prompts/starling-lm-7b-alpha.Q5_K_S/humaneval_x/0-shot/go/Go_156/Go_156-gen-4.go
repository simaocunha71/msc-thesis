    roman := make([]string, 0, 1001)
    roman = append(roman, "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix")
    roman = append(roman, "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "ix")
    roman = append(roman, "c", "ci", "cii", "ciii", "civ", "cv", "cvi", "cvii", "cviii", "cix")
    roman = append(roman, "l", "li", "lii", "liii", "liv", "lv", "lvi", "lvii", "lviii", "lix")
    roman = append(roman, "xl", "xli", "xlii", "xliv", "xlv", "xlvi", "xlvii", "xlviii", "xlix")
    roman = append(roman, "cxl", "cxli", "cxlii", "cxliv", "cxlv", "cxlvi", "cxlvii", "cxlvi", "cxlix")
    roman = append(roman, "xc", "xc", "xc", "xc", "xc")
    roman = append(roman, "m", "mi", "mii", "miii", "miv", "mv", "mvi", "mvii", "mviii", "mix")
    roman = append(roman, "xm", "xmi", "xmii", "xmiv", "xmv", "xmvi", "xmvii", "xmvi", "xmix")
    roman = append(roman, "cm", "cmi", "cmii", "cmiv", "cml", "cml", "cmvi", "cml", "cmi")
    roman = append(roman, "mm", "mm")

    result := ""
    for i := 1000; i >= 0; i-- {
        for j := 0; j < number/i; j++ {
