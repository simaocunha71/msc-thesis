
has_close_elements
There are a number of issues with your implementation:

You use a label (A:) which is not permitted in C++. You should use a loop variable.
Your loop variable (i and j) is not scoped to the loop. This is a good practice to do. You should declare i and j inside the loop.
Your function doesn't check if the vector is empty.

Here is your code with the above issues fixed:
bool has_close_elements(vector<float> numbers, float threshold){
    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups
You have a bug in your code. The loop variable i is not scoped to the loop. You should declare i inside the loop. Also, you don't check if the input string is empty. Here is your code with the above issues fixed:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;

    for (size_t i = 0; i < paren_string.length(); ++i) {
        char chr = paren_string[i];
        if (chr == '(') {
            level += 1;
            current_paren += chr;
        }
        if (chr == ')') {
            level -= 1;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

truncate_number
This function is simple. You can use the fmodf function to get the fractional part of the number. Here is your code with the above issues fixed:
float truncate_number(float number){
    return fmodf(number, 1.0f);
}

max