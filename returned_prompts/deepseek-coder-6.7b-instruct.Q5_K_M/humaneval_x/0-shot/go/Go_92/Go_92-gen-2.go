
	xInt, xOk := x.(int)
	yInt, yOk := y.(int)
	zInt, zOk := z.(int)

	if !xOk || !yOk || !zOk {
		return false
	}

	if xInt + yInt != zInt {
		return false
	}

	return true
}

func main() {

	fmt.Println(AnyInt(5, 2, 7))  // ➞ true
	fmt.Println(AnyInt(3, 2, 2))  // ➞ false
	fmt.Println(AnyInt(3, -2, 1))  // ➞ true
	fmt.Println(AnyInt(3.6, -2.2, 2))  // ➞ false
}

// 