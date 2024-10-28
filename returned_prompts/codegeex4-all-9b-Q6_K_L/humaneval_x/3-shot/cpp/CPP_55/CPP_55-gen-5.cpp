
has_close_elements
This function is on the right track, but it doesn't handle the case where numbers has only one element. You should check for this case and return false if that is the case.
Your nested for loop is fine, but it might be more efficient to put the if statement inside the inner loop and break out of the outer loop if you find a match. This way, you don't have to keep looping through the rest of the elements if you already found a match.
Here is the improved version:
bool has_close_elements(vector<float> numbers, float threshold) {
    if (numbers.size() <= 1) {
        return false;
    }

    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }

    return false;
}

separate_paren_groups
This function looks good, but it doesn't handle the case where there are multiple consecutive spaces in the input string. You should add a check for this case and skip over the spaces.
Here is the improved version:
vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for (i = 0; i < paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(') {
            level += 1;
            current_paren += chr;
        } else if (chr == ')') {
            level -= 1;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        } else if (chr != ' ') {
            // Skip over spaces
            continue;
        }
   