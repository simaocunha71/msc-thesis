    string result;
    for(int i=0; i<str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            result += (char)(str[i] - 32);
        }
        else if(str[i] >= 'A' && str[i] <= 'Z'){
            result += (char)(str[i] + 32);
        }
        else{
            result += str[i];
        }
    }
    return result;
}  // This function flips the case of a string. It goes through each character in the string, if the character is lowercase, it changes it to uppercase and if it is uppercase, it changes it to lowercase. If the character is neither lowercase nor uppercase, it leaves the character as it is. The function then returns the modified string.  // Note: This function assumes that the input string is not null and does not contain any characters other than ASCII letters.  // If you want to handle non-ASCII characters, you would need to use a more sophisticated approach.  // Also, this function is case-sensitive, so it would treat 'a' and 'A' as different characters.  // If you want to make it case-insensitive, you would need to convert the string to a standard case (like lowercase) before processing it.  // In that case, you would need to add some extra code to handle the conversion.  // For example, you could use the tolower() and toupper() functions from the C standard library.  // Here is an example of how you could do that:  // string filp_case(string str)  // {  //     string result;  //     for(int i=0; i<str.length(); i++){  //         if(islower(str[i]))  //             result += tolower(str[i]);  //         else if(isupper(str[i]))  //             result += toupper(str[i]);  //         else  //             result += str[i];  //     }  //     return result;  // }  // This version of the function is case-insensitive, so it would treat 'a' and 'A' as the same character.  // It uses the islower() and isupper() functions to check if a character is lowercase or uppercase, and the tolower() and toupper() functions to convert it to the other case.  // It then adds the converted character to the result string.  // If the character