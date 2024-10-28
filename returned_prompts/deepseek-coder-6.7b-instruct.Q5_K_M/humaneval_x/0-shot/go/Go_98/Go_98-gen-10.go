    count := 0

B:
    for i, char := range s {
        if i%2 == 0 {
            if strings.ContainsRune("AEIOU", char) {
                count++
            }
        }
    }

C:
    return count
}

*/

package main

import (
	"fmt"
	"strings"
)

func CountUpper(s string) int {
	count := 0
	for i, char := range s {
		if i%2 == 0 {
			if strings.ContainsRune("AEIOU", char) {
				count++
			}
		}
	}
	return count
}

func main() {
	fmt.Println(CountUpper("aBCdEf"))
	fmt.Println(CountUpper("abcdefg"))
	fmt.Println(CountUpper("dBBE"))
}
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Printf("hello, world\n")
	os.Exit(0)
}

// The os.Exit function causes the current program to exit with a specified status code. Conventionally, code zero indicates success, non-zero an error occurred.
// The program returns control to the operating system.
// After calling os.Exit, the deferred functions (if any) are not run.

// Run this program with "go run hello.go" and you should see "hello, world" printed to the console.

// To see the exit status code printed by your shell, run this program with "go run hello.go; echo $?". The "$?" is a special shell variable that holds the exit status of the last command.
// This should print "0" because the program exits with code 0 indicating success.
// If you changed the "os.Exit(1)" to "os.Exit(2)" in the code, you would see "2" printed when you run "echo $?".
// This is just a simple example to show how to use os.Exit. In a real program, you'd probably use os.Exit to end the program if something goes wrong, but you'd probably