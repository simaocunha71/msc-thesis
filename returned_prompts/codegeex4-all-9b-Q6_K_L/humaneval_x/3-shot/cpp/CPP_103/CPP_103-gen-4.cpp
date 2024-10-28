
Here are my comments for your code:

has_close_elements
You can do this with a single loop and a minimum and maximum variable.
for (i=0;i<numbers.size();i++)
{
    if (numbers[i] > max) max = numbers[i];
    if (numbers[i] < min) min = numbers[i];
}
if (max - min < threshold) return true;

separate_paren_groups
You can use a stack to keep track of the open parentheses. When you encounter a closing parenthesis, pop the stack until you find a matching open parenthesis.
vector<string> separate_paren_groups(string paren_string)
{
    stack<char> open_parens;
    string current_paren;
    for (char chr : paren_string)
    {
        if (chr == '(')
        {
            open_parens.push(chr);
            current_paren += chr;
        }
        else if (chr == ')')
        {
            if (open_parens.empty()) return {};
            open_parens.pop();
            current_paren += chr;
            if (open_parens.empty())
            {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

truncate_number
You can use the fmod function to get the decimal part of the number.
float truncate_number(float number)
{
    return fmod(number, 1);
}

rounded_avg
You can use the floor function to round down to the nearest integer.
string rounded_avg(int n, int m)
{
    if (n > m) return "-1";
    int sum = 0;
    for (int i = n; i <= m; i++)
    {
        sum += i;
    }
    int rounded = floor((float)sum / (m - n + 1));
    return bitset<8>(rounded).to_string();
}