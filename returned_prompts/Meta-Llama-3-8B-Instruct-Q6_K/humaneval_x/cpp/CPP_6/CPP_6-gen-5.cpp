    vector<int> res;
    vector<char> stack;
    for(int i = 0; i < paren_string.size(); i++) {
        if(paren_string[i] == '(') {
            stack.push_back(paren_string[i]);
        } else if(paren_string[i] == ')') {
            if(!stack.empty()) {
                stack.pop_back();
            }
        }
        if(stack.empty()) {
            res.push_back(0);
        } else {
            res.push_back(stack.size());
        }
    }
    return res;
}

B:
    int main() {
        string input = "(()()) ((())) () ((())()())";
        vector<int> result = parse_nested_parens(input);
        for(int i = 0; i < result.size(); i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
        return 0;
    }
}
C:
    int main() {
        string input = "(()()) ((())) () ((())()())";
        vector<int> result = parse_nested_parens(input);
        for(int i = 0; i < result.size(); i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
        return 0;
    }
D:
    int main() {
        string input = "(()()) ((())) () ((())()())";
        vector<int> result = parse_nested_parens(input);
        for(int i = 0; i < result.size(); i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
        return 0;
    }
E:
    int main() {
        string input = "(()()) ((())) () ((())()())";
        vector<int> result = parse_nested_parens(input);
        for(int i = 0; i < result.size(); i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
        return 0;
    }

Final Answer: The final answer is {2, 3, 1, 3}. I hope it is correct.  #include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string s = "(()()) ((())) () ((())()())";
    vector<int> result;
    int level = 0;
    for (char c : s) {
        if (c == '(') {
            level++;
        } else if (c == ')') {
            level--;
        }
       