    res := make([]int, len(game))

B:
    for i := range game {
        res[i] = int(math.Abs(float64(game[i] - guess[i])))
    }

C:
    return res
}
`

func TestCompare(t *testing.T) {
	type args struct {
		game  []int
		guess []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "Test 1",
			args: args{
				game:  []int{1, 2, 3, 4, 5, 1},
				guess: []int{1, 2, 3, 4, 2, -2},
			},
			want: []int{0, 0, 0, 0, 3, 3},
		},
		{
			name: "Test 2",
			args: args{
				game:  []int{0, 5, 0, 0, 0, 4},
				guess: []int{4, 1, 1, 0, 0, -2},
			},
			want: []int{4, 4, 1, 0, 0, 6},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Compare(tt.args.game, tt.args.guess); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Compare() = %v, want %v", got, tt.want)
			}
		})
	}
}

func BenchmarkCompare(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Compare([]int{0, 5, 0, 0, 0, 4}, []int{4, 1, 1, 0, 0, -