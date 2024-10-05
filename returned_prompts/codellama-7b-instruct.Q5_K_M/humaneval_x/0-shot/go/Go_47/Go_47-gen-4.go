	sort.Ints(l)

B:
	n := len(l)

C:
	if n == 0 {
		return 0
	}

D:
	if n == 1 {
		return 0
	}

E:
	if n == 2 {
		return 0
	}

F:
	mean := float64(l[n/2])

G:
