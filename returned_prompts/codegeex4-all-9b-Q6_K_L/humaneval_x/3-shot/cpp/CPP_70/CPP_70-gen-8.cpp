
Here are some comments on your code:
has_close_elements()

You're doing a lot of work inside your nested for loops.  You only need to do it once per pair.  So, you could do something like this:

bool has_close_elements(vector<float> numbers, float threshold) {
    for (auto i = numbers.begin(); i != numbers.end(); ++i) {
        for (auto j = i + 1; j != numbers.end(); ++j) {
            if (abs(*i - *j) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups()

This is a nice function.  You could make it a bit more efficient by using a stringstream instead of a string to hold the current paren group.  You can then just push_back the result instead of making a new string.  It would look like this:

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    stringstream current_paren;
    int level = 0;
    char chr;
    for (int i = 0; i < paren_string.size(); ++i) {
        chr = paren_string[i];
        if (chr == '(') {
            ++level;
            current_paren << chr;
        } else if (chr == ')') {
            --level;
            current_paren << chr;
            if (level == 0) {
                all_parens.push_back(current_paren.str());
                current_paren.str("");
            }
        }
    }
    return all_parens;
}

truncate_number()

This is fine.  It's doing what it's supposed to do.  Just remember that the result of this function will be a floating point number.

strange_sort_list()

This is a very clever function.  I like it.  You could make it a bit more efficient by using an iterator to the current min/max value instead of calling min_element and max_element.  This would look like this:

vector<int> strange_sort_list(vector<int> lst)