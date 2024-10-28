
Code review
First of all, you should use an appropriate include for the math library. You're using the abs() function, which is not defined in stdio.h. So your code should start with:
#include <cmath>

Also, your code is missing a #include <string> for the string class.
I'd also recommend that you use a for loop instead of a while loop for the separate_paren_groups() function. A for loop is usually easier to read and understand, and can be more efficient. And you should use the size() member function instead of .length() for the string class. So your code should look like this:
#include <cmath>
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (size_t i = 0; i < paren_string.size(); i++) {
        char chr = paren_string[i];
        if (chr == '(') {
            level++;
            current_paren += chr;
        } else if (chr == ')') {
            level--;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

Also, in your separate_paren_groups() function, you should check if the input string is empty before entering the loop. Otherwise, you'll end up with an empty string in the vector, and you may want to avoid that. So your code should look like this:
#include <cmath>
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    if (paren_string.empty()) {
        return all_parens;
    }
    for (size_t i = 0; i < paren_string.size(); i++) {
        char chr = paren_string[i];
        if (chr == '(') {
            level++;
            current_paren += chr;
        } else if (chr == ')