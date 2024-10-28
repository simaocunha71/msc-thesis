	binary := ""
	if decimal == 0 {
		return "db0000000db"
	}

B:
	for decimal > 0 {
		remainder := decimal % 2
		binary = fmt.Sprintf("%d%s", remainder, binary)
		decimal = decimal / 2
	}

C:
	return "db" + binary + "db"
}


func main() {
	fmt.Println(DecimalToBinary(15))
	fmt.Println(DecimalToBinary(32))
}


// Q2:

