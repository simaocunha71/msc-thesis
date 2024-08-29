#include <algorithm>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<string> all_prefixes(string str) {
    vector<string> result;
    for (int i = 0; i < str.length(); i++) {
        string prefix = str.substr(0, i + 1);
        result.push_back(prefix);
    }
    return result;
}

int main() {
    string input = "abc";
    vector<string> prefixes = all_prefixes(input);
    for (const auto& prefix : prefixes) {
        cout << prefix << " ";
    }
    cout << endl;
    return 0;
}