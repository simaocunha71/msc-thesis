    // split the string on the dot
    split_name := strings.Split(file_name, ".")

    // check if there is exactly one dot in the file's name
    if len(split_name) != 2 {
        return "No"
    }

    // check if there are more than 3 digits in the file's name
    digit_count := strings.Count(split_name[0], "0123456789")
    if digit_count > 3 {
        return "No"
    }

    // check if the file's name starts with a letter
    first_char := split_name[0][0]
    if first_char < 'a' || (first_char > 'z' && first_char < 'A') || first_char > 'Z' {
        return "No"
    }

    // check if the extension is one of these:  ['txt',  'exe',  'dll']
    switch split_name[1] {
    case "txt", "exe", "dll":
        return "Yes"
    default:
        return "No"
    }
}

The function works by splitting the file name at the dot, and checking if there is exactly one dot. It then counts the number of digits in the file name, and checks if this is less than or equal to 3. It then checks if the first character is a letter. Finally, it checks if the file's extension is one of the specified types.
*/

package main

import (
	"fmt"
)

func FileNameCheck(file_name string) string {
	split_name := strings.Split(file_name, ".")
	if len(split_name) != 2 {
		return "No"
	}
	digit_count := strings.Count(split_name[0], "0123456789")
	if digit_count > 3 {
		return "No"
	}
	first_char := split_name[0][0]
	if first_char < 'a' || (first_char > 'z' && first_char < 'A') || first_char