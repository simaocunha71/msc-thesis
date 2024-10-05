
Overall, your code looks pretty good.  The indentation is consistent and the variable names are clear.  There are a few things you could improve though:

In your has_close_elements function, you can break out of the loop as soon as you find two numbers that are closer together than the threshold.  There's no need to continue checking the rest of the array.
In your separate_paren_groups function, you should check if the character is a space before adding it to the current_paren string.
In your truncate_number function, you should return a value of 0.0 instead of 0.0 when the input is 0.0.
In your count_upper function, you should check if the character is a vowel before checking if it's uppercase.  This will prevent the function from returning an incorrect value if the character is an uppercase consonant.

Here's the modified code:

bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == ' ') {
            continue;
        }
        if (chr == '(') {
            level += 1;
        }
        current_paren += chr;
        if (chr == ')' && level == 0) {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
    return all_parens;
}

float truncate_number(float number){
    if (number == 0.0) {
        return 0.0;
    }
    return number - int(number);
}

int count_upper(string s){
    int upper = 0;
    for (char chr : s) {
       