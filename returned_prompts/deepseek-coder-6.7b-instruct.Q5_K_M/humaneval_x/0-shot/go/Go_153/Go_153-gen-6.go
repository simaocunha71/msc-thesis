  strongest := "StrongestExtension"
  max_strength := math.MinInt64
  for _, extension := range extensions {
      CAP, SM := 0, 0
      for _, c := range extension {
          if 'A' <= c && c <= 'Z' {
              CAP++
          } else if 'a' <= c && c <= 'z' {
              SM++
          }
      }
      strength := CAP - SM
      if strength > max_strength {
          max_strength = strength
          strongest = extension
      }
  }
  return class_name + "." + strongest
}

*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(StrongestExtension("my_class", []string{"AA", "Be", "CC"}))
}

func StrongestExtension(class_name string, extensions []string) string {
	strongest := class_name + "." + extensions[0]
	max_strength := 0
	for _, extension := range extensions {
		CAP, SM := 0, 0
		for _, c := range extension {
			if 'A' <= c && c <= 'Z' {
				CAP++
			} else if 'a' <= c && c <= 'z' {
				SM++
			}
		}
		strength := CAP - SM
		if strength > max_strength {
			max_strength = strength
			strongest = class_name + "." + extension
		}
	}
	return strongest
}

// Answers:
// For the given problem, the solution is to go through each extension and calculate its strength. If the strength is larger than the current maximum strength, update the maximum strength and the strongest extension. Finally, return the class name and the strongest extension in the required format.
// The strength of an extension is calculated as the difference between the count of uppercase letters (CAP) and the count of lowercase letters (SM).
// If there is a tie in strengths, the first extension encountered is considered the strongest.
// This solution is written in Go programming language.
// The time complexity of the