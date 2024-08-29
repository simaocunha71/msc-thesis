#include <algorithm>
#include <iterator>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

string pre = "";
vector<string> all_prefixes(string str){
    vector<string> out;
    for(int i = 0; i < str.length(); i++){
        pre += str[i];
        out.push_back(pre);
    }
    return out;
}

vector<string> all_prefixes(string str){
    vector<string> out;
    for(int i = 0; i < str.length(); i++){
        out.push_back(str.substr(0, i + 1));
    }
    return out;
}

int main(){
    vector<string> out = all_prefixes("abcdefg");
    for(int i = 0; i < out.size(); i++){
        cout << out[i] << endl;
    }
    return 0;
}