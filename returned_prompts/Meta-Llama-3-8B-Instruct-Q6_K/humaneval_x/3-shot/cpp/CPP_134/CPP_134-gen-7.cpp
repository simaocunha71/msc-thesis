    if(txt.length()==0 || txt[txt.length()-1]==' ')
        return false;
    if(isalpha(txt[txt.length()-1]))
        return true;
    return false;
}
//Note: You can use the following function to check if a character is alphabetical
//bool isalpha(char c) {
//    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
//}
//This is a simple and straightforward solution, but it can be improved by checking for
//the last character of the string after removing any trailing spaces. This can be done
//using the rfind function, which returns the position of the last occurrence of a specified
//character in a string. Here is the improved version:
//bool check_if_last_char_is_a_letter(string txt) {
//    string trimmed = txt.substr(0, txt.find_last_not_of(' ') + 1);
//    if(trimmed.length()==0 || trimmed[trimmed.length()-1]==' ')
//        return false;
//    if(isalpha(trimmed[trimmed.length()-1]))
//        return true;
//    return false;
//}
//This improved version should work correctly even if the input string has trailing spaces.