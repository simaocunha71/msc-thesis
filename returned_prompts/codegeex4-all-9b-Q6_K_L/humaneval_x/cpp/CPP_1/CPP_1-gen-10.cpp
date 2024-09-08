#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> paren_groups;
    string current_group;
    int depth = 0;

    for (char c : paren_string) {
        if (c == '(') {
            if (depth == 0) {
                current_group.clear();
            }
            depth++;
            current_group += c;
        } else if (c == ')') {
            depth--;
            current_group += c;
            if (depth == 0) {
                paren_groups.push_back(current_group);
                current_group.clear();
            }
        }
    }

    return paren_groups;
}

int main() {
    string input = "( ) (( )) (( )( ))";
    vector<string> output = separate_paren_groups(input);

    for (const string& group : output) {
        printf("\"%s\"\n", group.c_str());
    }

    return 0;
}
