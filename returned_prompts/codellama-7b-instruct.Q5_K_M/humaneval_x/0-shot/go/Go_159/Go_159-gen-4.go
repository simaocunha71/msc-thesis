
// You can modify the code below
// var number, need, remaining int
// number = 5
// need = 6
// remaining = 10
// fmt.Println(Eat(number, need, remaining))
// return

	res := make([]int, 2)

	if remaining < need {
		res[0] = number + remaining
		res[1] = 0
		return res
	}

	if remaining >= need {
		res[0] = number + need
		res[1] = remaining - need
		return res
	}

	return res
}
