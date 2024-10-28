func LargestSmallestIntegers(lst []int) [2]interface{}{

	var neg int
	var pos int
	var negflag bool
	var posflag bool

	for _, v := range lst {
		if v < 0 {
			negflag = true
			if neg == 0 || neg > v {
				neg = v
			}
		}
		if v > 0 {
			posflag = true
			if pos == 0 || pos < v {
				pos = v
			}
		}
	}

	if !negflag {
		neg = 0
	}

	if !posflag {
		pos = 0
	}

	return [2]interface{}{neg, pos}
}