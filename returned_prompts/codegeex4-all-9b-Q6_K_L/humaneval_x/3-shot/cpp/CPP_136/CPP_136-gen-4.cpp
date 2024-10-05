
has_close_elements

Your code is correct, but there's a few things that could be improved:

You should use braces for the for loop, even if they aren't needed. This makes your code more uniform and easier to read.
You should use the standard library function std::abs instead of the C function abs.
You should use the standard library function std::size instead of the member function size.
You should use a range-based for loop.

Here's a refactored version of your code:
bool has_close_elements(const std::vector<float>& numbers, float threshold) {
    for (auto i = numbers.begin(); i != numbers.end(); ++i) {
        for (auto j = i + 1; j != numbers.end(); ++j) {
            if (std::abs(*i - *j) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups

Your code is correct, but there's a few things that could be improved:

You should use braces for the for loop, even if they aren't needed. This makes your code more uniform and easier to read.
You should use the standard library function std::isdigit instead of the C function isdigit.
You should use the standard library function std::push_back instead of the member function push_back.
You should use a range-based for loop.

Here's a refactored version of your code:
std::vector<std::string> separate_paren_groups(const std::string& paren_string) {
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    char chr;
    for (auto chr : paren_string) {
        if (chr == '(') {
            ++level;
            current_paren += chr;
        } else if (chr == ')') {
            --level;
            current_paren += chr;
            if (level == 0) {
                all_p