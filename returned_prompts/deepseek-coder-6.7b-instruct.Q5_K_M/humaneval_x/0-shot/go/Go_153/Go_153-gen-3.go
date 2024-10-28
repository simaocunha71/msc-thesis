    var max_strength float64 = math.MinInt64
    var strongest_extension string

    for _, extension := range extensions {
        var strength float64 = 0
        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                strength++
            } else if char >= 'a' && char <= 'z' {
                strength--
            }
        }

        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }

    return class_name + "." + strongest_extension
}


func main() {
    fmt.Println(StrongestExtension("my_class", []string{"AA", "Be", "CC"}))
}


The function StrongestExtension calculates the strength of each extension by iterating through the characters in the extension. If a character is an uppercase letter, it increases the strength by 1, if it is a lowercase letter it decreases the strength by 1. The extension with the highest strength is then returned.
*/

package main

import (
	"fmt"
	"math"
	"strings"
)

func StrongestExtension(class_name string, extensions []string) string {
	var max_strength float64 = math.MinInt64
	var strongest_extension string

	for _, extension := range extensions {
		var strength float64 = float64(strings.Count(extension, "A")+strings.Count(extension, "a")) - float64(strings.Count(extension, "B")+strings.Count(extension, "b")+strings.Count(extension, "C")+strings.Count(extension, "c")+strings.Count(extension, "D")+strings.Count(extension, "d")+strings.Count(extension, "E")+strings.Count(extension, "e")+strings.Count(extension, "F")+strings.Count(extension, "f")+strings.Count(extension, "G")+strings.Count(extension, "g")+strings.Count(extension, "H")+strings.Count(extension, "h")+strings.Count(extension, "I")+