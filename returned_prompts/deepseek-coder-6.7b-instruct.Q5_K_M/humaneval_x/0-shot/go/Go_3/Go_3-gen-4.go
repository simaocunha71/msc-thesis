
    balance := 0

    for _, op := range operations {
        balance += op
        if balance < 0 {
            return true
        }
    }

    return false
}
*/

func TestBelowZero(t *testing.T) {
	tests := []struct {
		name        string
		operations  []int
		expectedOut bool
	}{
		{"Test 1", []int{1, 2, 3}, false},
		{"Test 2", []int{1, 2, -4, 5}, true},
		{"Test 3", []int{-1, 2, 3, 4, 5}, true},
		{"Test 4", []int{1, 2, 3, 4, 5}, false},
		{"Test 5", []int{}, false},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			out := BelowZero(test.operations)
			if out != test.expectedOut {
				t.Errorf("Expected %t but got %t", test.expectedOut, out)
			}
		})
	}
}

func BenchmarkBelowZero(b *testing.B) {
	operations := []int{1, 2, -4, 5}
	for i := 0; i < b.N; i++ {
		BelowZero(operations)
	}
}

func BelowZero(operations []int) bool {

	balance := 0

	for _, op := range operations {
		balance += op
		if balance < 0 {
			return true
		}
	}

	return false
}

/*
func main() {
	operations := []int{1, 2, 3}
	fmt.Println(BelowZero(operations))
	operations = []int{1, 2, -4, 5}
	fmt.Println(BelowZero(operations))
}
*/

// go test -v
// go test -bench=.
// go run main.