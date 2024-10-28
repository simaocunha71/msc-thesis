
balance := 0

for i := 0; i < len(operations); i++ {

balance += operations[i]

if balance < 0 {
return true
}
}

return false
}
*/

func BelowZero(operations []int) bool {
	balance := 0

	for _, operation := range operations {
		balance += operation
		if balance < 0 {
			return true
		}
	}

	return false
}

func main() {
	operations := []int{1, 2, 3}
	fmt.Println(BelowZero(operations)) // false

	operations = []int{1, 2, -4, 5}
	fmt.Println(BelowZero(operations)) // true
}

/*
