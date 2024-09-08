#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> filtered;
    for(auto str : strings){
        if(str.find(prefix) == 0){
            filtered.push_back(str);
        }
    }
    return filtered;
}

int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> filtered = filter_by_prefix(strings, prefix);
    for(auto str : filtered){
        cout << str << endl;
    }
    return 0;
}
