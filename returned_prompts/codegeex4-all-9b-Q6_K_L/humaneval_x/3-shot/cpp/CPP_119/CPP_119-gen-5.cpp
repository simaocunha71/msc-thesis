
A few minor things that could be improved:

You use the old C style for loop. In this case, it's not really necessary to use it, as the size() method returns the number of elements in the vector, which can be used directly in the condition of the for loop.
In the second question, you use a for loop with two variables, but in this case, you could simply use a single variable, as you don't need to access the elements of the vector directly. Instead, you could use the iterator of the vector to access the elements.
In the third question, you could use the fmod function from the math.h library to get the decimal part of the number, instead of subtracting the integer part from the original number.

Here's the updated code:

bool has_close_elements(vector<float> numbers, float threshold){
    for (auto i = numbers.begin(); i != numbers.end(); ++i) {
        for (auto j = i + 1; j != numbers.end(); ++j) {
            if (abs(*i - *j) < threshold) {
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
    char chr;
    for (auto i = paren_string.begin(); i != paren_string.end(); ++i) {
        chr = *i;
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

float truncate_number(float number){
    return fmod