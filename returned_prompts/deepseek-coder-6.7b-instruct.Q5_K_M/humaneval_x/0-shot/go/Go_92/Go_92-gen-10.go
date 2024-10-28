
	_, ok1 := x.(float64)
	_, ok2 := y.(float64)
	_, ok3 := z.(float64)

	if ok1 || ok2 || ok3 {
		return false
	}

	sum := int(x.(float64)) + int(y.(float64)) + int(z.(float64))

	if int(x.(float64)) == sum || int(y.(float64)) == sum || int(z.(float64)) == sum {
		return true
	}

	return false
}

func main() {
	fmt.Println(AnyInt(5, 2, 7))
	fmt.Println(AnyInt(3, 2, 2))
	fmt.Println(AnyInt(3, -2, 1))
	fmt.Println(AnyInt(3.6, -2.2, 2))
}

// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
//