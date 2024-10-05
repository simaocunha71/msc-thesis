	for _, v := range num {
		switch v {
		case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F':
		default:
			return 0
		}
	}

	var count int
	for _, v := range num {
		switch v {
		case '0':
			count++
		case '1':
			count++
		case '2':
			count++
		case '3':
			count++
		case '4':
			count++
		case '5':
			count++
		case '6':
			count++
		case '7':
			count++
		case '8':
			count++
		case '9':
			count++
		case 'A':
			count++
		case 'B':
			count++
		case 'C':
			count++
		case 'D':
			count++
		case 'E':
			count++
		case 'F':
			count++
		}
	}

	return count
}
