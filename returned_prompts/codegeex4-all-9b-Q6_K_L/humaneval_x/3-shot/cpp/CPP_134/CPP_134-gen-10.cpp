
I'll start with the last one. There is no need to check if the text is empty, because if it is, the return value will be false anyway. The same applies to the check if the character is a letter. That can be simplified to just checking the ASCII value of the character. If the last character is not a letter, the function will return false, otherwise it will return true. This reduces the code to just one line:
bool check_if_last_char_is_a_letter(string txt) {
    return !txt.empty() && (txt.back() >= 'a' && txt.back() <= 'z' || txt.back() >= 'A' && txt.back() <= 'Z');
}

The first one can be made much more efficient by sorting the array first. That way, you only need to check the first and last elements and can return false immediately if they are not within the threshold of each other. If you sort the array, the function will look like this:
bool has_close_elements(vector<float> numbers, float threshold) {
    sort(numbers.begin(), numbers.end());
    return numbers.size() >= 2 && numbers.front() + threshold >= numbers.back();
}

The second one can be improved by adding a check to see if the input string is empty. That way, the function will return an empty vector immediately if the input string is empty. Otherwise, it will loop through the string and add each group of parentheses to the vector. This reduces the code to just a few lines:
vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            ++level;
        }
        if (chr == ')') {
            --level;
        }
        current_paren += chr;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }
    return all_parens;
}

The third one can be simplified by