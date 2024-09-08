#include <iostream>
#include <map>
#include <string>
using namespace std;

map<char, int> histogram(string test) {
    map<char, int> histogram;
    if (test.empty()) {
        return histogram;
    }
    for (size_t i = 0; i < test.size(); ++i) {
        char c = test[i];
        histogram[c]++;
    }
    map<char, int> result;
    int max = 0;
    for (auto it = histogram.begin(); it != histogram.end(); ++it) {
        if (it->second > max) {
            result.clear();
            result.insert(*it);
            max = it->second;
        } else if (it->second == max) {
            result.insert(*it);
        }
    }
    return result;
}

int main() {
    map<char, int> result = histogram("a b c");
    for (auto it = result.begin(); it != result.end(); ++it) {
        cout << it->first << " " << it->second << endl;
    }
    return 0;
}