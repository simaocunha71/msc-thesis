
has_close_elements

The function name has a good name, but the parameter name could be better.  numbers is clear, but threshold could be better named as epsilon.
The function uses abs, which is more common when dealing with integers.  You should use fabs instead.
The function uses a for loop which is good, but you can use a range based for loop instead.
The function uses a goto, which is generally considered a bad practice.  Instead, you should use a boolean flag to indicate if a close pair was found and return early.
The function returns a bool, which is a good practice.

Here is a revised version of the function:
bool has_close_elements(const vector<float>& numbers, float epsilon) {
    bool found = false;
    for (auto i = numbers.begin(); i != numbers.end() && !found; ++i) {
        for (auto j = i + 1; j != numbers.end() && !found; ++j) {
            if (fabs(*i - *j) < epsilon) {
                found = true;
            }
        }
    }
    return found;
}

separate_paren_groups

The function name is good, but the parameter name could be better named as paren_string.
The function uses a for loop which is good, but you can use a range based for loop instead.
The function uses a goto, which is generally considered a bad practice.  Instead, you should use a boolean flag to indicate if a close pair was found and return early.
The function returns a vector of strings, which is a good practice.

Here is a revised version of the function:
vector<string>