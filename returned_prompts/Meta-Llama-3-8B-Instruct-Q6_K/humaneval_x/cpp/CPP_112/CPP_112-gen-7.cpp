    vector<string> result;
    string temp = "";
    for(int i=0; i<s.length(); i++){
        if(find(c.begin(), c.end(), s[i]) == c.end()){
            temp += s[i];
        }
    }
    result.push_back(temp);
    string t = temp;
    reverse(t.begin(), t.end());
    if(t == temp){
        result.push_back("True");
    }else{
        result.push_back("False");
    }
    return result;
}

int main(){
    string s = "abcdedcba";
    string c = "ab";
    vector<string> result = reverse_delete(s,c);
    for(int i=0; i<result.size(); i++){
        printf("%s\n",result[i].c_str());
    }
    return 0;
}
B:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> reverse_delete(string s, string c) {
    vector<string> result;
    string temp = "";
    for (char c : s) {
        if (find(c, c.begin(), c.end()) == c.end()) {
            temp += c;
        }
    }
    result.push_back(temp);
    string t = temp;
    reverse(t.begin(), t.end());
    if (t == temp) {
        result.push_back("True");
    } else {
        result.push_back("False");
    }
    return result;
}

int main() {
    string s = "abcdedcba";
    string c = "ab";
    vector<string> result = reverse_delete(s, c);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> reverse_delete(string s, string c) {
    vector<string> result;
    string temp = "";
    for (char c : s) {
        if (find(c, c.begin(), c.end()) == c.end()) {
            temp += c;
        }
    }
    result.push_back(temp);
    string t = temp;
    reverse(t.begin(), t.end());
    if (t == temp) {
        result.push_back("True");
    } else {
        result.push_back("False");
    }
    return result;
}

int main() {
    string s = "abcdedcba";
    string