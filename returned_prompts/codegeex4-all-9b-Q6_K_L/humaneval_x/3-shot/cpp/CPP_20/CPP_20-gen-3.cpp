
I'll check each of the functions for you.

has_close_elements

The logic is correct, but it could be improved in terms of readability and efficiency.  It is more efficient to break out of the loop as soon as a pair of close elements is found.
The function could be rewritten as:
bool has_close_elements(vector<float> numbers, float threshold)
{
    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            if (fabs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups

The logic is correct, but it could be improved in terms of readability and efficiency.  The function could be rewritten as:
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            ++level;
        } else if (chr == ')') {
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

truncate_number

The logic is correct, but it could be improved in terms of readability and efficiency.  The function could be rewritten as:
float truncate_number(float number)
{
    return number - (int)number;
}

find_closest_elements

The logic is correct, but it could be improved in terms of readability and efficiency.  The function could be rewritten as:
vector<float> find_closest_elements(vector<float> numbers)
{
   