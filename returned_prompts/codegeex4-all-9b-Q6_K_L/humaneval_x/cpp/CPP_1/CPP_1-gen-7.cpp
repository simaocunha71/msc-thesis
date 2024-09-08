#include <vector>
#include <string>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    string current;
    int depth = 0;
    for (char c : paren_string) {
        if (c == '(') {
            depth++;
            if (depth == 1) {
                current.clear();
            }
        } else if (c == ')') {
            depth--;
            if (depth == 0) {
                result.push_back(current);
            }
        } else if (depth > 0) {
            current.push_back(c);
        }
    }
    return result;
}

B:
#include <vector>
#include <string>
#include <stack>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<int> depth;
    string current;
    for (char c : paren_string) {
        if (c == '(') {
            depth.push(result.size());
            current.clear();
        } else if (c == ')') {
            result[depth.top()] = current;
            depth.pop();
        } else {
            current.push_back(c);
        }
    }
    return result;
}

C:
#include <vector>
#include <string>
#include <stack>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<int> depth;
    string current;
    for (char c : paren_string) {
        if (c == '(') {
            depth.push(result.size());
            current.clear();
        } else if (c == ')') {
            result[depth.top()] = current;
            depth.pop();
        } else {
            current.push_back(c);
        }
    }
    return result;
}

D:
#include <vector>
#include <string>
#include <stack>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<int> depth;
    string current;
    for (char c : paren_string) {
        if (c == '(') {
            depth.push(result.size());
            current.clear();
        } else if (c == ')') {
            result[depth.top()] = current;
            depth.pop();
        } else {
            current.push_back(c);
        }
    }
    return result;
}

E:
#include <vector>
#include <string>
#include <stack>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
   