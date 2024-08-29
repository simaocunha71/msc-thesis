#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

string longest(vector<string> strings) {
    if(strings.empty()) {
        return string();
    }
    string longest = strings[0];
    for(size_t i = 1; i < strings.size(); ++i) {
        if(strings[i].size() > longest.size()) {
            longest = strings[i];
        }
    }
    return longest;
}

int main() {
    vector<string> strings;
    printf("%s\n", longest(strings).c_str());
    strings.push_back("a");
    strings.push_back("b");
    strings.push_back("c");
    printf("%s\n", longest(strings).c_str());
    strings.clear();
    strings.push_back("a");
    strings.push_back("bb");
    strings.push_back("ccc");
    printf("%s\n", longest(strings).c_str());
    return 0;
}
