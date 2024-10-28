
The first thing I would suggest is to use descriptive names for variables and functions.  This makes it easier to understand what the code is intended to do without having to read and understand the entire function.  So, for example:
bool has_close_elements(vector<float> numbers, float threshold)
{
    for (int i=0; i<numbers.size(); i++)
    {
        for (int j=i+1; j<numbers.size(); j++)
        {
            if (abs(numbers[i]-numbers[j])<threshold)
            {
                return true;
            }
        }
    }
    return false;
}

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level=0;
    for (int i=0; i<paren_string.length(); i++)
    {
        char chr = paren_string[i];
        if (chr=='(')
        {
            level += 1;
            current_paren += chr;
        }
        if (chr==')')
        {
            level -= 1;
            current_paren += chr;
            if (level==0)
            {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

float truncate_number(float number)
{
    return number-int(number);
}

int digitSum(string s)
{
    int i, ascii_sum = 0;
    for (i=0; i<s.length(); i++)
    {
        if (s[i]>=65 && s[i]<=90)
        {
            ascii_sum += int(s[i]);
        }
    }
    return ascii_sum;
}

The second thing I would suggest is to add comments to your code.  This makes it easier for someone else (or yourself in a few months) to understand what your code is supposed to be doing.  So, for example:
/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close_elements({1.0, 2.0, 3.0}, 0.5)
false
>>> has_close_elements({1.0, 2.8, 3.