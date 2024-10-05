
I see a few issues.  Let's take a look at each function.
1) has_close_elements
This function appears to work, but it's not the most efficient way to implement it.  You're currently using a nested loop, which results in O(n^2) time complexity.  You can do this in O(n log n) time using a sort and a single pass.
Here's a refactored version:
bool has_close_elements(vector<float> numbers, float threshold) {
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size() - 1; i++) {
        if (numbers[i+1] - numbers[i] < threshold) {
            return true;
        }
    }
    return false;
}

2) separate_paren_groups
This function is correct, but it's not very efficient.  You're currently iterating through the entire string, which results in O(n) time complexity.  You can do this in O(n) time using a single pass.
Here's a refactored version:
vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            level++;
        } else if (chr == ')') {
            level--;
        }
        current_paren += chr;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
    return all_parens;
}

3) truncate_number
This function is correct, but it's not very efficient.  You're currently using the int() cast, which results in O(n) time complexity.  You can do this in O(1) time