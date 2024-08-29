#include <iostream>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> parse_nested_parens(string paren_string) {
        vector<int> result;
        if (paren_string.empty()) return result;

        stack<int> s;
        stringstream ss(paren_string);
        string tmp;
        while (getline(ss, tmp, ' ')) {
            int level = 0, max_level = 0;
            for (char c : tmp) {
                if (c == '(') {
                    level++;
                    max_level = max(max_level, level);
                }
                else if (c == ')') {
                    level--;
                }
            }
            result.push_back(max_level);
        }
        return result;
    }
};

int main() {
    Solution sol;
    string paren_string = "(()()) ((())) () ((())()())";
    vector<int> result = sol.parse_nested_parens(paren_string);
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}