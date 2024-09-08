    // Check if string is empty
    if(txt.empty()) return false;

    // Check if the last character is a letter
    if(isalpha(txt.back())) {
        // Check if the last character is part of a word
        if(txt.find(' ') == string::npos || txt.find(' ', 0, txt.size()) == txt.size()) {
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
    printf("%d\n", check_if_last_char_is_a_letter(test1)); // false
    printf("%d\n", check_if_last_char_is_a_letter(test2)); // true
    printf("%d\n", check_if_last_char_is_a_letter(test3)); // false
    printf("%d\n", check_if_last_char_is_a_letter(test4)); // false
    return 0;
}