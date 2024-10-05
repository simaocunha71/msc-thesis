
has_close_elements
You're missing the include for std::abs and you're missing a semicolon at the end of the function declaration.
Also, this is a simple enough function that it could benefit from a more idiomatic loop structure:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups
You're not checking for unbalanced parentheses.  This can be done by checking that level is 0 at the end of the loop.
Also, you're missing the include for std::string and std::vector.
Lastly, you're returning a vector of strings.  This is not idiomatic C++ for returning containers, and it's not clear why you're not returning a std::ostringstream.  If you're not going to return a std::ostringstream, you should return a std::vector<std::string> instead of a vector<string>.
Also, you're not checking for unbalanced parentheses.  This can be done by checking that level is 0 at the end of the loop.
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for (i = 0; i < paren_string.length(); ++i) {
        chr = paren_string[i];
        if (chr == '(') {
            ++level;
            current_paren += chr;
        } else if (chr == ')') {
            --level;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }

    if (level != 0) {
        // Handle unbalanced parentheses
    }

    return all_parens;
}

truncate_number
You're using a floating point number in an integer context, which is not a good idea.  You should cast the result of int() to a float.
float truncate_number(float number){
    return number - (float)int(number);
}

triangle_area
You're not including the include