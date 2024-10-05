	for i, v := range num {
		if v >= '0' && v <= '9' {
			continue
		}
		if v >= 'A' && v <= 'F' {
			if v == 'A' {
				num = num[:i] + "10" + num[i+1:]
			} else if v == 'B' {
				num = num[:i] + "11" + num[i+1:]
			} else if v == 'C' {
				num = num[:i] + "12" + num[i+1:]
			} else if v == 'D' {
				num = num[:i] + "13" + num[i+1:]
			} else if v == 'E' {
				num = num[:i] + "14" + num[i+1:]
			} else if v == 'F' {
				num = num[:i] + "15" + num[i+1:]
			}
			goto A
		}
	}

	// fmt.Println(num)

	for i, v := range num {
		if v >= '0' && v <= '9' {
			if i == 0 {
				continue
			}
			if num[i-1] == '1' {
				num = num[:i-1] + "0" + num[i:]
				goto A
			}
			if num[i-1] == '2' {
				num = num[:i-1] + "1" + num[i:]
				goto A
			}
			if num[i-1] == '3' {
				num = num[:i-1] + "2" + num[i:]
				goto A
			}
			if num[i-1] == '4' {
				