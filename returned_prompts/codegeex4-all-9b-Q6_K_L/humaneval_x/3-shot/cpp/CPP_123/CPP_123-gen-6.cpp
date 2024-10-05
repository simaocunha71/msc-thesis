
has_close_elements
Your code is not well-formed, because your function does not return a value. If there are no elements within the threshold, the function will implicitly return 0, which will be treated as false. Instead, you should return false explicitly.
Furthermore, your function is not efficient. It's easy to see that your function has a quadratic time complexity, because you're comparing each pair of elements twice. You can reduce this to linear time complexity by using a single loop, and keeping track of the minimum and maximum value that you have seen so far.
bool has_close_elements(vector<float> numbers, float threshold)
{
    float min_val = numbers[0];
    float max_val = numbers[0];
    for (size_t i = 1; i < numbers.size(); ++i)
    {
        if (numbers[i] < min_val)
            min_val = numbers[i];
        else if (numbers[i] > max_val)
            max_val = numbers[i];
    }
    return max_val - min_val < threshold;
}

separate_paren_groups
Your code is not well-formed, because you're trying to use a character as a string. This will cause a compilation error. You should use string concatenation instead.
Also, your code is not efficient. It's easy to see that your function has a quadratic time complexity, because you're trying to find the level of each closing parenthesis. You can reduce this to linear time complexity by using a stack.
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string)
    {
        if (chr == '(')
        {
            ++level;
            current_paren += chr;
        }
        else if (chr == ')')
        {
            --level;
            current_paren += chr;
            if (level == 0