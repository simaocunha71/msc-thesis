    if (txt.empty())
        return false;
    if (!isalpha(txt[txt.length() - 1]))
        return false;
    if (txt.length() > 1 && isalpha(txt[txt.length() - 2]))
        return false;
    return true;
}

int main(){
    printf("%d\n", check_if_last_char_is_a_letter("apple pie"));
    printf("%d\n", check_if_last_char_is_a_letter("apple pi e"));
    printf("%d\n", check_if_last_char_is_a_letter("apple pi e "));
    printf("%d\n", check_if_last_char_is_a_letter(""));
    return 0;
}

Explanation:
This function first checks if the string is empty. If it is, it returns false. Then it checks if the last character is a letter. If it is not, it returns false. It then checks if the second last character is a letter. If it is, it returns false. If none of these conditions are met, it returns true. This means that the last character is a letter that is not part of a word.
*/

#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool check_if_last_char_is_a_letter(char *txt){
    int len = strlen(txt);
    if (len == 0)
        return false;
    if (!isalpha(txt[len - 1]))
        return false;
    if (len > 1 && isalpha(txt[len - 2]))
        return false;
    return true;
}

int main(){
    printf("%d\n", check_if_last_char_is_a_letter("apple pie"));
    printf("%d\n", check_if_last_char_is_a_letter("apple pi e"));
    printf("%d\n", check_if_last_char_is_a_letter("apple pi e "));
    printf("%d\n", check_if_last_char_is_a_letter(""));
    return 0;