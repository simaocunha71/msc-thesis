    vector<string> v;
    string tmp="";
    for(int i=0;i<s.length();i++){
        if(find(c.begin(),c.end(),s[i])==c.end()){
            tmp+=s[i];
        }
    }
    v.push_back(tmp);
    return v;
}
vector<string> check_palindrome(string s){

    string tmp="";
    for(int i=s.length()-1;i>=0;i--){
        tmp+=s[i];
    }
    if(s==tmp)return vector<string>{s,"True"};
    else return vector<string>{s,"False"};
}
int main(){
    string s,c;
    cin>>s>>c;
    vector<string> ans=reverse_delete(s,c);
    vector<string> tmp=check_palindrome(ans[0]);
    printf("%s %s",ans[0].c_str(),tmp[1].c_str());
}

*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> delete_and_check(string s, string c) {
    vector<string> v;
    string tmp = "";
    for (int i = 0; i < s.length(); i++) {
        if (find(c.begin(), c.end(), s[i]) == c.end()) {
            tmp += s[i];
        }
    }
    v.push_back(tmp);
    return check_palindrome(tmp);
}

vector<string> check_palindrome(string s) {
    string tmp = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        tmp += s[i];
    }
    if (s == tmp) return vector<string>{s, "True"};
    else return vector<string>{s, "False"};
}

int main() {
    string s, c;
    cin >> s >> c;
    vector<string> ans = delete