
Your has_close_elements function can be made more efficient by breaking out of the loop as soon as you find that a pair of numbers are closer than the threshold.  This will reduce the worst case time complexity from O(n^2) to O(n), where n is the number of elements in the vector.
Also, there is no need for an explicit loop counter variable.  You can use the range-based for loop in C++11, which is more idiomatic for iterating over containers.
Here's a revised version:
bool has_close_elements(const vector<float>& numbers, float threshold) {
    for (auto it = numbers.begin(); it != numbers.end() - 1; ++it) {
        for (auto it2 = it + 1; it2 != numbers.end(); ++it2) {
            if (abs(*it - *it2) < threshold) {
                return true;
            }
        }
    }
    return false;
}

Your separate_paren_groups function can be simplified by using the string::find and string::substr functions.  This will reduce the number of string comparisons and index calculations.  Here's a revised version:
vector<string> separate_paren_groups(const string& paren_string) {
    vector<string> all_parens;
    size_t pos = 0;
    while (pos != string::npos) {
        pos = paren_string.find_first_of('(', pos);
        if (pos != string::npos) {
            size_t end_pos = paren_string.find_first_of(')', pos);
            if (end_pos != string::npos) {
                all_parens.push_back(paren_string.substr(pos, end_pos - pos + 1));
                pos = end_pos + 1;
            } else {
                break;
            }
        }
    }
    return all_parens;
}

Your truncate_number function is correct, but it can be simplified by using the fmod function from the math library.  Here's a revised version:
float truncate_number(float number) {
    return fmod(number, 1.0f);
}

Your add function is correct, but it can be simplified by using the + operator.  Here's a revised version:
int add(int x, int y) {
    return x + y;
