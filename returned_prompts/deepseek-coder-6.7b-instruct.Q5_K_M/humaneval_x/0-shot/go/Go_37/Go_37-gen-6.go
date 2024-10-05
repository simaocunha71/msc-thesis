	sort.Ints(l)
	for i:=0; i<len(l); i+=2 {
		l[i] = l[i+1]
	}
	return l
}


