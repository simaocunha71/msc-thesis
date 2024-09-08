#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> new_strings;
    for (int i = 0; i < strings.size(); i++){
        if (strings[i].substr(0, prefix.size()) == prefix){
            new_strings.push_back(strings[i]);
        }
    }
    return new_strings;
}
int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    vector<string> filtered_strings = filter_by_prefix(strings, "a");
    for (int i = 0; i < filtered_strings.size(); i++){
        cout << filtered_strings[i] << endl;
    }
    return 0;
}
