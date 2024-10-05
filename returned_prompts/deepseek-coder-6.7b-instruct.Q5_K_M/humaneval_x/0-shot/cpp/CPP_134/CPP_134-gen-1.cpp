bool check_if_last_char_is_a_letter(string txt){
    if (txt.empty()) return false;
    char lastChar = txt[txt.size() - 1];
    if (!isalpha(lastChar)) return false;
    if (txt.size() == 1) return true;
    char secondLastChar = txt[txt.size() - 2];
    return !isalpha(secondLastChar);
}

/*
The function first checks if the string is empty and returns false if so. It then gets the last character of the string and checks if it's a letter. If it isn't, it returns false. If the string only contains one character, it returns true. Finally, it gets the second last character of the string and checks if it's a letter. If it is, it returns false. If all these checks pass, it returns true.
*/

// QUESTION 2
/*
