#include<stdio.h>
#include<string>
using namespace std;
bool check_if_last_char_is_a_letter(string txt){

    // Get the last character of the string
    char last_char = txt[txt.length() - 1];

    // Check if the last character is a letter
    if (isalpha(last_char)) {

        // Check if the last character is not part of a word
        if (txt.length() == 0 || txt[txt.length() - 1] == ' ') {
            return true;
        }
    }

    return false;
}

int main() {

    string test1 = "apple pie";
    string test2 = "apple pi e";
    string test3 = "apple pi e ";
    string test4 = "";

    printf("Test 1: %s\n", check_if_last_char_is_a_letter(test1) ? "true" : "false");
    printf("Test 2: %s\n", check_if_last_char_is_a_letter(test2) ? "true" : "false");
    printf("Test 3: %s\n", check_if_last_char_is_a_letter(test3) ? "true" : "false");
    printf("Test 4: %s\n", check_if_last_char_is_a_letter(test4) ? "true" : "false");

    return 0;
}

