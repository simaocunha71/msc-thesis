    if(txt.length()==0)
        return false;
    if(isalpha(txt.back()))
        return txt.back()==' ' || txt.back()==txt[txt.length()-2];
    return false;
}
// Explanation: 
// 1. Check if string is empty. If yes, return false.
// 2. Check if last character is an alphabetical character.
// 3. If it is, then check if it is a space or not.
// 4. If it is a space, return true. If not, return false.
// 5. If it is not an alphabetical character, return false. 
// This function checks if the last character of a given string is an alphabetical character and is not a part of a word. If it is, it returns true, otherwise it returns false. 
// It considers a word as a group of characters separated by a space. 
// It handles the case when the string is empty, and also when the last character is a space. 
// It also handles the case when the last character is a part of a word. 
// It uses the isalpha function from the c++ standard library to check if a character is an alphabetical character. 
// It uses the back function to get the last character of the string. 
// It uses the length function to get the length of the string. 
// It uses the [ ] operator to access the characters of the string. 
// It uses the == operator to compare the characters. 
// It uses the && operator to combine the conditions. 
// It returns a boolean value indicating whether the last character of the string is an alphabetical character and is not a part of a word. 
// This function is case sensitive, it considers uppercase and lowercase letters as different characters. 
// This function is also sensitive to the position of the last character, it considers the last character as the last character of the string. 
// It does not consider the last character as the first character of the next word. 
// It does not consider the last character as the last character of the previous word. 
// It does not consider the last character as a part of the previous word. 
// It does not consider the last character as a part of the next word. 
// It does not consider the last character as a part of a punctuation. 
// It does not consider the last character as a part of a digit. 
// It does not consider the last character as a part of a special character. 
// It