#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> all_prefixes(string str) {
    vector<string> result;
    for (int i = 0; i < str.length(); i++) {
        result.push_back(str.substr(0, i+1));
    }
    return result;
}

int main() {
    string str = "abc";
    vector<string> prefixes = all_prefixes(str);
    for (string prefix : prefixes) {
        cout << prefix << endl;
    }
    return 0;
}
