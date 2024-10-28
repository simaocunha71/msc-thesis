
This code is not correct. You cannot compare floating point numbers using the == operator. You must use an epsilon value to compare two floating point numbers. Here is how you can do it:
if (abs(numbers[i]-numbers[j]) < threshold)
    return true;

I have no idea what you are trying to achieve with the following code. It seems like you are trying to check if the parentheses string is balanced, but you are not doing it correctly. Here is how you can do it:
bool is_balanced(string s) {
    int level = 0;
    for (char c : s) {
        if (c == '(') {
            level++;
        } else if (c == ')') {
            level--;
            if (level < 0) {
                return false;
            }
        }
    }
    return level == 0;
}

void separate_paren_groups(string paren_string, vector<string>& all_parens) {
    string current_paren;
    int level = 0;
    char chr;
    for (int i = 0; i < paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(') {
            level++;
            current_paren += chr;
        } else if (chr == ')') {
            level--;
            current_paren += chr;
            if (level == 0) {
                if (is_balanced(current_paren)) {
                    all_parens.push_back(current_paren);
                }
                current_paren = "";
            }
        }
    }
}

This code is not correct. You are checking if a number is the multiplication of three prime numbers, but you are not doing it correctly. Here is how you can do it:
bool is_prime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
   