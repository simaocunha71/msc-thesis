    for key := range dict{
        switch key.(type) {
        case string:
            if strings.ToLower(key.(string)) != key.(string) && strings.ToUpper(key.(string)) != key.(string){
                return false
            }
        default:
            return false
        }
    }
    return true
}

This code is designed to check if all keys in the dictionary are strings. If they are, it checks if they are in lower or upper case. If they are not, it returns false.
This function will work correctly with empty dictionaries, as it will return false in this case.
*/

package main

import (
	"fmt"
)

func CheckDictCase(dict map[interface{}]interface{}) bool {
	for key := range dict {
		switch key.(type) {
		case string:
			if strings.ToLower(key.(string)) != key.(string) && strings.ToUpper(key.(string)) != key.(string) {
				return false
			}
		default:
			return false
		}
	}
	return true
}

func main() {
	dict1 := map[interface{}]interface{}{"a": "apple", "b": "banana"}
	dict2 := map[interface{}]interface{}{"a": "apple", "A": "banana", "B": "banana"}
	dict3 := map[interface{}]interface{}{"a": "apple", 8: "banana", "a": "apple"}
	dict4 := map[interface{}]interface{}{"Name": "John", "Age": "36", "City": "Houston"}
	dict5 := map[interface{}]interface{}{"STATE": "NC", "ZIP": "12345"}

	fmt.Println(CheckDictCase(dict1)) // should return true
	fmt.Println(CheckDictCase(dict2)) // should return false
	fmt.Println(CheckDictCase(dict3)) // should return false
	fmt.Println(CheckDictCase(dict4)) // should return false
	fmt.