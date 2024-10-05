    m := make(map[rune]int)
    for _, letter := range test {
        if _, ok := m[letter]; ok {
            m[letter]++
        } else {
            m[letter] = 1
        }
    }

B:
    max := 0
    for _, v := range m {
        if v > max {
            max = v
        }
    }

C:
    result := make(map[rune]int)
    for k, v := range m {
        if v == max {
            result[k] = v
        }
    }

    return result
}


A: 
In this step, we create a map that counts the number of times each character appears in the input string.

B: 
In this step, we find the maximum count among all the characters.

C: 
In this step, we return a map that contains only the characters that appear the maximum number of times.


A: 
Here, we create a map that counts the number of times each character appears in the input string.

B: 
In this step, we find the maximum count among all the characters.

C: 
Here, we return a map that contains only the characters that appear the maximum number of times.


A: 

B: 

C: 


The function "Histogram" takes a string as input and returns a map with the frequency of each character. The function starts by creating an empty map. Then it iterates over each character in the string and increments the corresponding value in the map. If the character is not in the map yet, it is added with a value of 1. 

Next, it finds the maximum frequency. 

Finally, it creates a new map that contains only the characters that have the maximum frequency and returns it. 

If the input string is empty, the function returns an empty map.
*/

func Histogram(test string) map[rune]int {

	m := make(map[rune]int)
	for _, letter := range test {
		if _, ok := m[letter]; ok {
			m[letter]++
		} else