#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<string> groups;
    string current_group;

    for (char c : paren_string) {
        if (c == '(') {
            groups.push(current_group);
            current_group = "";
        } else if (c == ')') {
            current_group += ")";
            if (!groups.empty()) {
                current_group = groups.top() + current_group;
                groups.pop();
            }
            result.push_back(current_group);
            current_group = "";
        } else {
            current_group += c;
        }
    }

    return result;
}

int main() {
    vector<string> groups = separate_paren_groups("( ) (( )) (( )( ))");
    for (const auto& group : groups) {
        cout << "\"" << group << "\"" << endl;
    }
    return 0;
}

B:
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    string current_group;

    for (char c : paren_string) {
        if (c == '(') {
            result.push_back(current_group);
            current_group = "(";
        } else if (c == ')') {
            current_group += ")";
            result.push_back(current_group);
            current_group = "";
        } else {
            current_group += c;
        }
    }

    return result;
}

int main() {
    vector<string> groups = separate_paren_groups("( ) (( )) (( )( ))");
    for (const auto& group : groups) {
        cout << "\"" << group << "\"" << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<string> groups;
    string current_group;

    for (char c : paren_string) {
        if (c == '(') {
            groups.push(current_group);
            current_group = "";
        } else if (c == ')') {
            current_group += ")";
            if (!groups.empty()) {
                current_group = groups.top() + current_group;
                groups.pop();
            }
            result.push_back(current_group);
            current_group = "";
        } else {
            current_group += c;
       