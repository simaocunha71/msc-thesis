	for i := range l {
		for j := range l {
			for k := range l {
				if i == j || i == k || j == k {
					continue
				}
				if l[i]+l[j]+l[k] == 0 {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	fmt.Println(TriplesSumToZero([]int{1, 2, 3, 7}))
}
