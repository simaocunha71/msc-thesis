
There are a couple of things wrong with your has_close_elements function:

The return type is bool, but your function returns a pointer to a bool.
You're not using the threshold parameter anywhere.
You're not handling the case where the vector is empty.

Here's a corrected version:
bool has_close_elements(vector<float> numbers, float threshold) {
    if (numbers.size() < 2) {
        return false;
    }

    for (size_t i = 0; i < numbers.size() - 1; ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (fabs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }

    return false;
}

Your separate_paren_groups function is mostly correct, but you're not handling the case where there are spaces in the input string. You should remove them before processing the string. Here's a corrected version:
vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for (i = 0; i < paren_string.length(); ++i) {
        chr = paren_string[i];
        if (chr == '(' || chr == ')') {
            if (chr == '(') {
                level += 1;
            } else {
                level -= 1;
            }
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

Your truncate_number function is correct.

Your reverse_delete function is mostly correct, but you're not handling the case where the input string is empty. Here's a corrected version:
vector<string> reverse_delete(string s, string c) {
    string result = "";
    for (size_t i = 0; i < s.length(); ++i) {
       