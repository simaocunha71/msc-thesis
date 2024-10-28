
// We first determine the length of the string
len := len(s)

B:

// Then we check if it is a prime number
for i := 2; i*i <= len; i++ {
    if len%i == 0 {
        return false
    }
}

C:

return true

}

*/

package main

import (
	"fmt"
)

func PrimeLength(s string) bool {

	len := len(s)

	for i := 2; i*i <= len; i++ {
		if len%i == 0 {
			return false
		}
	}

	return true

}

func main() {

	fmt.Println(PrimeLength("Hello"))
	fmt.Println(PrimeLength("abcdcba"))
	fmt.Println(PrimeLength("kittens"))
	fmt.Println(PrimeLength("orange"))
}
package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"testing"
)

func TestMain(m *testing.M) {
	dir, err := ioutil.TempDir("", "test")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer os.RemoveAll(dir)

	os.Chdir(dir)

	os.Exit(m.Run())
}

func Test_create(t *testing.T) {
	type args struct {
		path string
		name string
	}
	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{
			name: "test create",
			args: args{
				path: ".",
				name: "test.txt",
			},
			wantErr: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
		