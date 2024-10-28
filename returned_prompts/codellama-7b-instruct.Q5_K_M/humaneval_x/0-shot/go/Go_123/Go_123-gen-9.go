	for {
		if n%2 == 0 {
			n = n / 2
		} else if n%2 == 1 {
			n = 3*n + 1
		}
		if n == 1 {
			break A
		}
	}
	return []int{1, n}
}

func main() {
	fmt.Println(GetOddCollatz(5))
	fmt.Println(GetOddCollatz(7))
}
