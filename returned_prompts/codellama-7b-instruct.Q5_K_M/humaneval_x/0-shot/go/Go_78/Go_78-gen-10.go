	for _, c := range num {
		switch c {
		case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F':
			// do nothing
		default:
			continue A
		}
		switch c {
		case '2', '3', '5', '7', 'B', 'D':
			// do nothing
		default:
			continue A
		}
		fmt.Println("Hit a prime:", string(c))
	}

	return 0
}
