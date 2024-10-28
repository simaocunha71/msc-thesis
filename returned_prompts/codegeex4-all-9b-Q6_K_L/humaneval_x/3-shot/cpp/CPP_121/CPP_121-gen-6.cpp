
This one is pretty easy.  Your code doesn't work because you're trying to increment the vector index with a float value.  You need to increment the index by one every iteration.  Change:
for (i=0;i<numbers.size();i+=0.5)
for (j=i+1;j<numbers.size();j+=0.5)

To:
for (i=0;i<numbers.size();i++)
for (j=i+1;j<numbers.size();j++)

This one is a bit trickier, but the basic idea is that you're looking for a string of characters between two parentheses.  You need to keep track of whether or not the parentheses you're currently looking at have been closed or not.  Here's some code that should work:
#include <vector>
#include <string>
#include <cctype>

std::vector<std::string> separate_paren_groups(std::string paren_string) {
    std::vector<std::string> all_parens;
    std::string current_paren;
    char chr;
    for (std::size_t i = 0; i < paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(') {
            current_paren += chr;
        } else if (chr == ')') {
            current_paren += chr;
            if (current_paren.length() > 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

This function works by iterating over the input string.  If it encounters an open parenthesis, it adds it to the current string.  If it encounters a close parenthesis, it adds it to the current string and checks to make sure that the current string isn't empty.  If it's not, it adds the current string to the list of all strings and resets the current string.  If it encounters anything else, it simply ignores it.

This one is pretty easy.  You just need to subtract the integer part of the number from the number itself.  Here's some code that should work:
float truncate_number(float number) {
    return number - static_cast<float>(static_cast<int>(number));
}

This function works