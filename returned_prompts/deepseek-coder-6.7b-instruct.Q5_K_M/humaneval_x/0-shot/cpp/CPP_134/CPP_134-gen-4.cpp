    if(txt.empty()) return false;
    if(!isalpha(txt.back())) return false;
    if(txt.length()==1) return true;
    if(txt[txt.length()-2] != ' ') return true;
    return false;
}


int main()
{
    printf(check_if_last_char_is_a_letter("apple pie") ? "true" : "false"); // ➞ false
    printf("\n");
    printf(check_if_last_char_is_a_letter("apple pi e") ? "true" : "false"); // ➞ true
    printf("\n");
    printf(check_if_last_char_is_a_letter("apple pi e  ") ? "true" : "false"); // ➞ false
    printf("\n");
    printf(check_if_last_char_is_a_letter("") ? "true" : "false"); // ➞ false
    printf("\n");
    return 0;
}



The function is checking if the last character of the string is a letter and not a part of a word.
It does this by first checking if the string is empty. If it is, it returns false.
Then, it checks if the last character of the string is a letter using the isalpha function. If it is not, it returns false.
If the string has only one character, it returns true.
Finally, it checks if the second to last character of the string is not a space. If it is not, it returns true. Otherwise, it returns false.
*/

// ➞ false, because "apple pie" does not end with a space, and "pie" is a word, not a letter.
// ➞ true, because "apple pi e" ends with a space after "e", and "e" is a letter.
// ➞ false, because "apple pi e  " ends with a space after "e", and "e" is a letter, but "e" is part of a word, not a letter.
// ➞ false, because the string is empty.
// ➞ false, because the string is empty.
// ➞