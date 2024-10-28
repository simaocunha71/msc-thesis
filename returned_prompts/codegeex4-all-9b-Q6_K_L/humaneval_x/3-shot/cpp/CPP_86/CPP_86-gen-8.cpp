
C++ doesn't support comments in the middle of statements.
In your first function, you don't need to declare the variables i and j before the loop, you can declare them in the for loop itself.  For example:
for (int i = 0; i < numbers.size(); i++) {
    for (int j = i + 1; j < numbers.size(); j++) {
        if (abs(numbers[i] - numbers[j]) < threshold) {
            return true;
        }
    }
}

In your second function, you should consider using a stringstream instead of a char to iterate over the string.  For example:
stringstream ss(paren_string);
char chr;
string current_paren;
int level = 0;
while (ss >> chr) {
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

In your third function, you don't need to cast the result of int(number) to float, because int(number) is already a float.  For example:
return number - int(number);

In your fourth function, you don't need to declare the variable i before the loop, you can declare it in the for loop itself.  For example:
for (int i = 0; i < s.length(); i++) {
    if (s[i] == ' ') {
        sort(current_word.begin(), current_word.end());
        result += current_word;
        result += s[i];
        current_word = "";
    } else {
        current_word += s[i];
    }
}

Finally, you should include the necessary headers at the top of your file.  For example:
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

And you should use the standard namespace