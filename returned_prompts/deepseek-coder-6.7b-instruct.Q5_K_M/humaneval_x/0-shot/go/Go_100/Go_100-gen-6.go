
  // Initialize array
  var arr []int = make([]int, n)

  // Loop through the array
  for i := 0; i < n; i++ {
    if n % 2 != 0 {
      arr[i] = n + i * 2
    } else {
      arr[i] = n + (i+1) * 2
    }
  }

  return arr
}

*/

package main

import (
	"fmt"
)

func MakeAPile(n int) []int {
	var arr []int = make([]int, n)
	for i := 0; i < n; i++ {
		if n%2 != 0 {
			arr[i] = n + i*2
		} else {
			arr[i] = n + (i+1)*2
		}
	}
	return arr
}

func main() {
	fmt.Println(MakeAPile(3))
}
package main

import "testing"

func TestMakeAPile(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "Test case 1",
			args: args{
				n: 3,
			},
			want: []int{3, 5, 7},
		},
		{
			name: "Test case 2",
			args: args{
				n: 4,
			},
			want: []int{4, 6, 8, 10},
		},
		{
			name: "Test case 3",
			args: args{
				n: 1,
			},
			want: []int{1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MakeAPile(tt.args.n); !equal(got, tt.want) {
