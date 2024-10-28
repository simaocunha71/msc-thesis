
Here's a quick review of your code.
Q1
Your solution is correct, but the code could be simplified a bit:
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

Q2
Your solution is correct, but it's not very efficient. You can solve the problem in a single pass:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char c : paren_string) {
        if (c == '(') {
            level++;
        } else if (c == ')') {
            level--;
        }
        current_paren += c;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
    return all_parens;
}

Q3
Your solution is correct, but it's not very efficient. You can solve the problem in a single pass:
float truncate_number(float number){
    return number - floor(number);
}

Q4
Your solution is not correct. The function boost::any_cast<int>(temp) will throw an exception if the value is not an int. You should use boost::any_cast<int>(temp).has_value() to check if the value is an int before casting it.
vector<int> filter_integers(list_any values){
    vector<int> result;
    for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
        boost::any temp = *it;
        if (boost::any_cast<int>(temp).has_value()) {
            result.push_back(boost::any_cast<int>(temp));
        }
    }
    return result;
