    result := ""
    for i:=0; i<=n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return strings.TrimSpace(result)
}

func main() {
    fmt.Println(StringSequence(5))
}

import  (
    "fmt"
    "strings"
    "strconv"
)

func StringSequence(n int) string{
    result := ""
    for i:=0; i<=n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return strings.TrimSpace(result)
}

func main() {
    fmt.Println(StringSequence(5))
}
*/
import (
	"fmt"
	"strings"
	"strconv"
)

func StringSequence(n int) string{
	result := ""
	for i:=0; i<=n; i++ {
		result += strconv.Itoa(i) + " "
	}
	return strings.TrimSpace(result)
}

func main() {
	fmt.Println(StringSequence(5))
}
/*
This program takes an integer n as input and returns a string containing space-delimited numbers starting from 0 upto n inclusive.
The function StringSequence(n int) uses a for loop to generate the sequence from 0 to n. 
The strconv.Itoa() function is used to convert each integer to a string. The result string is then trimmed using the strings.TrimSpace() function.
*/

/*
