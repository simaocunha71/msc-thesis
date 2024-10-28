    if strings.Count(file_name, ".") > 1 {
        return "No"
    }
    split := strings.Split(file_name, ".")
    if len(split) != 2 {
        return "No"
    }

B:
    if !(strings.ContainsAny(split[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") &&
        strings.ContainsAny(split[0], "0123456789")) {
        return "No"
    }
    if strings.Count(split[0], ".") > 1 || len(split[0]) == 0 {
        return "No"
    }

C:
    count := 0
    for _, char := range split[0] {
        if '0' <= char && char <= '9' {
            count++
        }
    }
    if count > 3 {
        return "No"
    }

D:
    if split[1] != "txt" && split[1] != "exe" && split[1] != "dll" {
        return "No"
    }

E:
    return "Yes"
}

The program should return 'Yes' for all valid files and 'No' for invalid ones. The conditions for validity are as stated in the problem. The file name should contain one dot and the file extension should be either 'txt', 'exe', or 'dll'. The part before the dot should contain only letters and at most 3 digits.
*/

package main

import (
	"fmt"
	"strings"
)

func FileNameCheck(file_name string) string {

	if strings.Count(file_name, ".") > 1 {
		return "No"
	}
	split := strings.Split(file_name, ".")
	if len(split) != 2 {
		return "No"
	}

	if !(strings.ContainsAny(split[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY