    // check if the input string is empty
    if(txt.empty()) return false;

    // get the last character of the string
    char last_char = txt.back();

    // check if the last character is an alphabetical character
    if(!isalpha(last_char)) return false;

    // check if the last character is part of a word
    // if the character before the last character is a space, then the last character is not part of a word
    if(txt.size() > 1 && txt[txt.size()-2] == ' ') return true;

    return false;
}

int main(){
    string txt;
    cout << "Enter a string: ";
    getline(cin, txt);

    bool result = check_if_last_char_is_a_letter(txt);

    if(result) cout << "The last character is a letter and is not part of a word." << endl;
    else cout << "The last character is not a letter or is part of a word." << endl;

    return 0;
}

C:
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Remove the newline character at the end of the string
    str[strcspn(str, "\n")] = 0;

    if (str[0] == '\0') {
        printf("The last character is not a letter or is part of a word.\n");
    } else {
        if (str[strlen(str) - 1] == ' ' || str[strlen(str) - 1] == '\0') {
            printf("The last character is not a letter or is part of a word.\n");
        } else if (isalpha(str[strlen(str) - 1])) {
            printf("The last character is a letter and is not part of a word.\n");
        } else {
            printf("The last character is not a letter or is part of a word.\n");
        }
    }

    return 0;
}

E:
```python
def check_if_last_char_is_a_letter(txt):
    if not txt:  # check if the input string is empty
        return False

    last_char = txt[-1]  # get the last character of the string

    if not last_char.isalpha():  # check if the last character is an alphabetical character
        return False

    if txt[-