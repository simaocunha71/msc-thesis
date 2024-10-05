    if text == "" {
        return nil
    }

    hasher := md5.New()
    hasher.Write([]byte(text))

    return fmt.Sprintf("%x", hasher.Sum(nil))
}

func main() {

    fmt.Println(StringToMd5("Hello world"))
}
*/

import (
	"crypto/md5"
	"fmt"
	"io"
)

// Given a string 'text', return its md5 hash equivalent string.
// If 'text' is an empty string, return "".
//
// >>> StringToMd5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
func StringToMd5(text string) string {
	if text == "" {
		return ""
	}

	hash := md5.New()
	io.WriteString(hash, text)
	return fmt.Sprintf("%x", hash.Sum(nil))
}

func main() {
	fmt.Println(StringToMd5("Hello world"))
}

// 