    if(txt.empty())
        return false;
    char last_char = txt.back();
    bool is_last_char_alphabetic = isalpha(last_char);
    bool is_last_char_part_of_word = false;
    for(int i = 0; i < txt.length() - 1; i++){
        if(txt[i] == ' ' && i == txt.length() - 2){
            is_last_char_part_of_word = true;
            break;
        }
    }
    return is_last_char_alphabetic && !is_last_char_part_of_word;
}

int main()
{
    printf("%d\n", check_if_last_char_is_a_letter("apple pie")); // ➞ false
    printf("%d\n", check_if_last_char_is_a_letter("apple pi e")); // ➞ true
    printf("%d\n", check_if_last_char_is_a_letter("apple pi e ")); // ➞ false
    printf("%d\n", check_if_last_char_is_a_letter("")); // ➞ false
    return 0;
}
