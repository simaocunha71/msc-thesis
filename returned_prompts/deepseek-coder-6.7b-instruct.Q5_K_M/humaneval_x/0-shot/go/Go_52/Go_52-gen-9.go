
// 1. Traverse the list l.
for _, number := range l {

// 2. If any number in the list is greater than or equal to the threshold t, return false.
if number >= t {
return false
}
}

// 3. If all numbers in the list are below the threshold t, return true.
return true
}

*/

func Test_BelowThreshold(t *testing.T) {

	type test struct {
		input []int
		thres int
		want  bool
	}

	tests := []test{
		{[]int{1, 2, 4, 10}, 100, true},
		{[]int{1, 20, 4, 10}, 5, false},
		{[]int{2, 8, 10, 15}, 12, false},
		{[]int{5, 4, 3, 2, 1}, 6, true},
	}

	for _, test := range tests {
		got := BelowThreshold(test.input, test.thres)
		if got != test.want {
			t.Errorf("Expected %t, got %t for input %v and threshold %d", test.want, got, test.input, test.thres)
		}
	}

}

func Test_BelowThreshold_Submission(t *testing.T) {

	type test struct {
		input []int
		thres int
		want  bool
	}

	tests := []test{
		{[]int{1, 2, 4, 10}, 100, true},
		{[]int{1, 20, 4, 10}, 5, false},
		{[]int{2, 8, 10, 15}, 12, false},
		{[]int{5, 4, 3, 2, 1}, 6, true},
	}

	for _, test := range tests {
		got := BelowThreshold(test.input, test.thres)
		if