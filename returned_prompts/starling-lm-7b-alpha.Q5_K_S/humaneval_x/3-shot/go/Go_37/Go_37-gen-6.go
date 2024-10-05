	even_index_values := l[0:len(l):2]
	sort.Ints(even_index_values)
	result := make([]int, len(l))
	for i, v := range l {
		result[i] = v
	}
	for i, v := range even_index_values {
		result[i*2+1] = v
	}
	return result
}



