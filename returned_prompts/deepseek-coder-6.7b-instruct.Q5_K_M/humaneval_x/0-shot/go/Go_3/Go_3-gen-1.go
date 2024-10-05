
balance := 0
for _, operation := range operations {
    balance += operation
    if balance < 0 {
        return true
    }
}
return false
}
*/

func TestBelowZero(t *testing.T) {
    tests := []struct {
        name string
        operations []int
        want bool
    }{
        {
            name: "Test 1",
            operations: []int{1, 2, 3},
            want: false,
        },
        {
            name: "Test 2",
            operations: []int{1, 2, -4, 5},
            want: true,
        },
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := BelowZero(tt.operations); got != tt.want {
                t.Errorf("BelowZero() = %v, want %v", got, tt.want)
            }
        })
    }
}

/*
