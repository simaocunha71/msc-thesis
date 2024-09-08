#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
using namespace std;

vector<string> filter_by_prefix(vector<string> strings, string prefix) {
    vector<string> result;
    copy_if(strings.begin(), strings.end(), back_inserter(result), [prefix](const string& str) { return str.find(prefix) == 0; });
    return result;
}

int main() {
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    vector<string> filtered = filter_by_prefix(strings, "a");
    for (const auto& str : filtered) {
        cout << str << " ";
    }
    cout << endl;
    return 0;
}
