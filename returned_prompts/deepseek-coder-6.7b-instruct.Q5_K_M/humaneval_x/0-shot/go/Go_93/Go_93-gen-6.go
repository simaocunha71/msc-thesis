     swapCase := ""
     for _, char := range message {
         if unicode.IsLower(char) {
             swapCase += strings.ToUpper(string(char))
         } else {
             swapCase += strings.ToLower(string(char))
         }
     }

B:
     vowels := "aeiouAEIOU"
     encodedMessage := ""
     for _, char := range swapCase {
         if strings.ContainsRune(vowels, char) {
             switch char {
             case 'a', 'A':
                 encodedMessage += "C"
             case 'e', 'E':
                 encodedMessage += "G"
             case 'i', 'I':
                 encodedMessage += "K"
             case 'o', 'O':
                 encodedMessage += "Q"
             case 'u', 'U':
                 encodedMessage += "S"
             }
         } else {
             encodedMessage += string(char)
         }
     }

     return encodedMessage
}

func main() {
    fmt.Println(Encode("test"))
    fmt.Println(Encode("This is a message"))
}


A: 
The first part of the function, swapCase, is used to swap the case of all letters. The unicode package in Go provides a function IsLower to check if a character is in lower case. If it is, the function ToUpper is used to convert it to upper case and vice versa.

B: 

The second part of the function, encodedMessage, is used to replace all the vowels in the message with the letter that appears 2 places ahead of that vowel in the english alphabet. A switch-case statement is used to match the vowels and replace them with the corresponding characters.

Note: This code assumes that the input message only contains letters and spaces. If there are any other characters, this code might not behave as expected.

This solution has a time complexity of O(n) because it iterates over the message once to swap the case and once to encode the message. The space complexity is also O(n) because it creates a new string to store the encoded message.
*/

// Test Cases:
// 1