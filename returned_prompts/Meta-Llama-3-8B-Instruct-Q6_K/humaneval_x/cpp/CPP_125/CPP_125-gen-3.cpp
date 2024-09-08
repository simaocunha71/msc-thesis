    vector<string> result;
    size_t pos = 0;
    while ((pos = txt.find(" ")) != string::npos) {
        result.push_back(txt.substr(0, pos));
        txt.erase(0, pos + 1);
    }
    if (txt.find(",") != string::npos) {
        size_t pos2 = txt.find(",");
        result.push_back(txt.substr(0, pos2));
        txt.erase(0, pos2 + 1);
    }
    if (txt.length() > 0)
        result.push_back(txt);
    int count = 0;
    for(int i = 0; i < 26; i++){
        if(txt.find(chr(i + 97)) != string::npos){
            count++;
        }
    }
    result.push_back(to_string(count));
    return result;

}
int main(){
    string txt = "Hello,world!";
    vector<string> result = split_words(txt);
    for(auto str : result){
        cout << str << endl;
    }
    return 0;
}
B:
    #include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> split_words(string s) {
    vector<string> result;
    size_t pos = 0;
    while ((pos = s.find(" ")) != string::npos) {
        result.push_back(s.substr(0, pos));
        s.erase(0, pos + 1);
    }
    if (s.find(",") != string::npos) {
        size_t pos2 = s.find(",");
        result.push_back(s.substr(0, pos2));
        s.erase(0, pos2 + 1);
    }
    if (!s.empty()) {
        result.push_back(s);
    }
    int count = 0;
    for (char c = 'a'; c <= 'z'; c++) {
        if (s.find(c) != string::npos) {
            count++;
        }
    }
    result.push_back(to_string(count));
    return result;
}

int main() {
    string s = "Hello,world!";
    vector<string> result = split_words(s);
    for (auto str : result) {
        cout << str << endl;
    }
    return 0;
}
C:
    #include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> split_words(string s) {
    vector<string> result;
    size