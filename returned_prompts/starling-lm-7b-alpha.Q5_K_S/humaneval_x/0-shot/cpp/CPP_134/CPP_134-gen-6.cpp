    for (int i=txt.length()-1; i>=0; i--) {
        if (txt[i] >= 'a' && txt[i] <= 'z') {
            if (i == txt.length()-1) {
                if (txt[i-1] == ' ' || txt[i-1] == '\0') {
                    return true;
                } else {
                    return false;
                }
            } else {
                if (txt[i-1] == ' ') {
                    return true;
                } else {
                    continue;
                }
            }
        } else {
            continue;
        }
    }
    return false;
}

/*
Explanation:
In this function, we check the last character of the given string and if it's an alphabetical
character, we check if it's a part of a word or not. If it's not a part of a word, we return true,
else return false.
To check if a given character is an alphabetical character, we use the ASCII values of alphabets
which range from 97 to 122 for lowercase alphabets and 65 to 90 for uppercase alphabets.
*/



/*
In the main function, we declare a string of our choice and pass it to the function check_if_last_char_is_a_letter.
Then, we print the result of the function call.
*/

int main() {
    string txt = "apple pie";
    printf("%d", check_if_last_char_is_a_letter(txt));
    return 0;
}

















































































































