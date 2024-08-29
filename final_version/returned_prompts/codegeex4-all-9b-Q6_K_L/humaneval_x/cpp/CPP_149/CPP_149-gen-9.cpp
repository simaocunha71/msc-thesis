#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> vector_sort(vector<string> lst) {
    // remove elements with odd lengths
    lst.erase(remove_if(lst.begin(), lst.end(), [](const string& s) { return s.size() % 2 != 0; }), lst.end());

    // sort the vector by length of each word and alphabetically
    sort(lst.begin(), lst.end(), [](const string& a, const string& b) {
        if (a.size() == b.size()) {
            return a < b;
        }
        return a.size() < b.size();
    });

    return lst;
}

int main() {
    vector<string> lst = {"ab", "a", "aaa", "cd"};
    vector<string> result = vector_sort(lst);
    for (const auto& str : result) {
        cout << str << " ";
    }
    cout << endl;
    return 0;
}
