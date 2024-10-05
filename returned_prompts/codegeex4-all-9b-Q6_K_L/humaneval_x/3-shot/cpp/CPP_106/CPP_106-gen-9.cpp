
This is a good start, but you're using goto and magic numbers and your code is a bit hard to follow.
// This could be a function parameter
const float EPSILON = 0.00001f;

bool has_close_elements(vector<float> numbers, float threshold)
{
    // This is more idiomatic in C++
    for (auto i = numbers.begin(); i != numbers.end(); ++i) {
        for (auto j = i + 1; j != numbers.end(); ++j) {
            if (abs(*i - *j) < threshold + EPSILON) {
                return true;
            }
        }
    }

    return false;
}

I've added a small epsilon to account for floating point imprecision.  It's not ideal, but it's the best I've got at the moment.
For your second question, you have a bug in your code, you're not checking to see if there's a matching closing parenthesis for each opening parenthesis.  You'll need to keep track of your level.
#include <stack>
#include <string>

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;

    for (i = 0; i < paren_string.length(); i++)
    {
        chr = paren_string[i];
        if (chr == '(') {
            level += 1;
            current_paren += chr;
        }
        else if (chr == ')') {
            level -= 1;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }

    return all_parens;
}

I've also changed your code to use a stack to keep track of your levels, this is easier to follow.
Your third question, you're not using any math