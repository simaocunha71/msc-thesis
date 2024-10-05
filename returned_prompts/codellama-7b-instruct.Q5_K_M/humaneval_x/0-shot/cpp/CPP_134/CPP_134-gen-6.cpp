if (txt.length() <= 0)
    return false;

if (isalpha(txt[txt.length() - 1])) {
    bool not_part_of_word = true;
    for (int i = 0; i < txt.length() - 1; i++) {
        if (txt[i] == txt[txt.length() - 1]) {
            not_part_of_word = false;
            break;
        }
    }
    return not_part_of_word;
}
return false;
}

int main() {
    string s("hello world");
    cout << check_if_last_char_is_a_letter(s) << endl;
    return 0;
}