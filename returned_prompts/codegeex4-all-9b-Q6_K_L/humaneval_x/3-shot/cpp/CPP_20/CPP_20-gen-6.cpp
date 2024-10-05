
This function is overly complicated.  You don't need to use a label to break out of the inner loop.  You should also consider using a range-based for loop to make it even simpler.
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); ++i){
        for (int j = i + 1; j < numbers.size(); ++j){
            if (abs(numbers[i] - numbers[j]) < threshold){
                return true;
            }
        }
    }
    return false;
}

This function is overly complicated.  You should consider using a range-based for loop to make it even simpler.
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;

    for (char chr : paren_string){
        if (chr == '('){
            ++level;
        }
        current_paren += chr;
        if (chr == ')'){
            --level;
            if (level == 0){
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }
    return all_parens;
}

This function is overly complicated.  You should consider using a range-based for loop to make it even simpler.
float truncate_number(float number){
    return number - static_cast<int>(number);
}

This function is overly complicated.  You should consider using a range-based for loop to make it even simpler.
vector<float> find_closest_elements(vector<float> numbers){
    vector<float> two_elements;
    float closest = 100000;
    for (int i = 0; i < numbers.size(); ++i){
        for (int j = i + 1; j < numbers.size(); ++j){
            if (abs(numbers[i] - numbers[j]) < closest){
                closest = abs(numbers[i] - numbers[j]);
                two_elements[0] = numbers[i