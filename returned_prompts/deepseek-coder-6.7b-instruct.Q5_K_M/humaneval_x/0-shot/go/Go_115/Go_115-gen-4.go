    return 0
}
`

func TestMaxFill(t *testing.T) {
	tests := []struct {
		name   string
		inputs []string
		output int
	}{
		{
			name: "Test 1",
			inputs: []string{
				"[[0,0,1,0], [0,1,0,0], [1,1,1,1]]",
				"1",
			},
			output: 6,
		},
		{
			name: "Test 2",
			inputs: []string{
				"[[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]",
				"2",
			},
			output: 5,
		},
		{
			name: "Test 3",
			inputs: []string{
				"[[0,0,0], [0,0,0]]",
				"5",
			},
			output: 0,
		},
	}

	program := `
func MaxFill(grid [][]int, capacity int) int {
	var steps int
	for _, row := range grid {
		for _, cell := range row {
			if cell == 1 {
				steps += (capacity - 1)
			}
		}
	}
	return steps
}
	`
	env := NewEnvironment(program)
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			grid, err := ParseIntMatrix(test.inputs[0])
			if err != nil {
				t.Errorf("Failed to parse grid: %v", err)
				return
			}
			capacity, err := strconv.Atoi(test.inputs[1])
			if err != nil {
				t.Errorf("Failed to parse capacity: %v", err)
				return
			}
			result := env.Execute("MaxFill", grid, capacity)
			if result.(int) !=