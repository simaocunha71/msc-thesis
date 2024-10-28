    for key, _ := range dict {
        switch key.(type) {
        case string:
            if strings.ToLower(key.(string)) != key.(string) &&
                strings.ToUpper(key.(string)) != key.(string) {
                return false
            }
        default:
            return false
        }
    }
    return true
}

The code above is a simple function that checks if the keys in a given dictionary are either all lower case or all upper case. The function iterates over the keys in the dictionary, checking if they are strings. If they are, it checks if they are all in lower case or all in upper case. If they are not all in either case, it returns false. If it manages to iterate over all keys without returning false, it returns true.

If the dictionary is empty, the function will return false as requested.
*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(CheckDictCase(map[interface{}]interface{}{"a": "apple", "b": "banana"}))
	fmt.Println(CheckDictCase(map[interface{}]interface{}{"a": "apple", "A": "banana", "B": "banana"}))
	fmt.Println(CheckDictCase(map[interface{}]interface{}{"a": "apple", 8: "banana", "a": "apple"}))
	fmt.Println(CheckDictCase(map[interface{}]interface{}{"Name": "John", "Age": "36", "City": "Houston"}))
	fmt.Println(CheckDictCase(map[interface{}]interface{}{"STATE": "NC", "ZIP": "12345"}))
}

func CheckDictCase(dict map[interface{}]interface{}) bool {
	if len(dict) == 0 {
		return false
	}

	for key, _ := range dict {
		switch key.(type) {
		case string:
			if strings.ToLower(key.(string)) != key.(string) &&
				strings.ToUpper(key.(string)) !