
//First, handle the edge case where n is 1. In this case, if x is also 1, then the function should return true. Otherwise, return false.
	if n == 1 {
		return x == 1
	}

//Second, handle the edge case where x is 0. In this case, the function should return true since 0 to any power is 0.
	if x == 0 {
		return true
	}

//Third, handle the edge case where x is negative. In this case, the function should return false since a negative number to any positive power would result in a negative number.
	if x < 0 {
		return false
	}

//Finally, calculate the integer power of n until it exceeds x. If the result of this calculation is x, then return true. Otherwise, return false.
	for i := 2; ; i++ {
		res := math.Pow(float64(n), float64(i))
		if res > float64(x) {
			return false
		} else if res == float64(x) {
			return true
		}
	}

}

```


## 3. Test Cases

```go
func TestIsSimplePower(t *testing.T) {

	type args struct {
		x int
		n int
	}

	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "Test 1",
			args: args{
				x: 1,
				n: 4,
			},
			want: true,
		},
		{
			name: "Test 2",
			args: args{
				x: 2,
				n: 2,
			},
			want: true,
		},
		{
			name: "Test 3",
			args: args{
				x: 8,
				n: 2,
			},
			want: true,
		},
		{
			name: "Test 4",
			args: args{
				x: 3,
			