
You have three questions, which you've asked in three different posts.  Stack Overflow is not a forum.  It's a Q&A site.  Each question should be in a single post.  You can edit your question to add new parts to it, but you should not ask new questions as separate posts.  If you have multiple questions about a single problem, you should ask them all in one post.  If you have multiple unrelated questions, you should ask them all in separate posts.
You've also asked three questions that are essentially the same thing.  I'm not sure why you've asked three of them.  If you have a general question about programming, you should ask it once.  If you have a specific problem that you're trying to solve, you should ask it once.  If you have multiple specific problems that you're trying to solve, you should ask them once each.
Here's a review of the code you've posted, in case you want it.  I've made some edits to make it more idiomatic C++:

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;
        }
    }
    return false;
}

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            ++level;
            current_paren += chr;
        } else