count := 0
for i := 1; i < n; i++ {
	if i%11 == 0 || i%13 == 0 {
		s := strconv.Itoa(i)
		for _, v := range s {
			if v == '7' {
				count++
			}
		}
	}
}
return count
}

