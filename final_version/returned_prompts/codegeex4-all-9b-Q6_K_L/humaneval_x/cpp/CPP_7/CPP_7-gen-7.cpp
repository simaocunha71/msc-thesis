#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> filter_by_substring(vector<string> strings, string substring){
    vector<string> filtered;
    for(auto str: strings){
        if(str.find(substring) != string::npos){
            filtered.push_back(str);
        }
    }
    return filtered;
}
int main(){
    vector<string> a = {"abc", "bacd", "cde", "vector"};
    auto b = filter_by_substring(a, "a");
    for(auto s: b){
        cout << s << endl;
    }
    return 0;
}

