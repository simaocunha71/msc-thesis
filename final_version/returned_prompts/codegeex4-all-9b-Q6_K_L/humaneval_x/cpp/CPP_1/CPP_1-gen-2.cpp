#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<char> s;
    string current_group = "";

    for (char c : paren_string) {
        if (c == '(') {
            s.push(c);
            current_group += c;
        } else if (c == ')') {
            if (!s.empty()) {
                s.pop();
                current_group += c;

                if (s.empty()) {
                    result.push_back(current_group);
                    current_group = "";
                }
            }
        }
    }

    return result;
}

int main() {
    vector<string> groups = separate_paren_groups("( ) (( )) (( )( ))");
    for (const string& group : groups) {
        cout << group << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<char> s;
    string current_group = "";

    for (char c : paren_string) {
        if (c == '(') {
            s.push(c);
            current_group += c;
        } else if (c == ')') {
            if (!s.empty()) {
                s.pop();
                current_group += c;

                if (s.empty()) {
                    result.push_back(current_group);
                    current_group = "";
                }
            }
        }
    }

    return result;
}

int main() {
    vector<string> groups = separate_paren_groups("( ) (( )) (( )( ))");
    for (const string& group : groups) {
        cout << group << endl;
    }
    return 0;
}
B:
#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<char> s;
    string current_group = "";

    for (char c : paren_string) {
        if (c == '(') {
            s.push(c);
            current_group += c;
        } else if (c == ')') {
            if (!s.empty()) {
                s.pop();
                current_group += c;

                if (s.empty()) {
                    result.push_back(current_group);
                    current_group = "";
                }
            }
        }
    }

    return result