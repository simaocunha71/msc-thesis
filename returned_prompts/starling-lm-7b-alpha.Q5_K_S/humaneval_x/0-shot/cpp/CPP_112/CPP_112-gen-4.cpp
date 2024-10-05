    vector<string>res;
    int i=0,j=s.length()-1;
    for(int k=0;k<s.length();k++){
        if(find(c.begin(),c.end(),s[k])!=c.end()){
            continue;
        }
        res.push_back(string(1,s[k]));
    }
    int n=res.size();
    while(i<j){
        if(res[i]!=res[j]){
            return vector<string>(2,"False");
        }
        i++;
        j--;
    }
    return vector<string>(2,res.begin()->append(res.end()));
}
int main(){
    string s="abcdedcba",c="ab";
    vector<string>res=reverse_delete(s,c);
    for(auto it:res)printf("%s ",it.c_str());
    return 0;
}

*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, c;
    cin >> s >> c;
    int i = 0, j = s.length() - 1;
    vector<string> res;
    while (i < j) {
        if (find(c.begin(), c.end(), s[i]) != c.end() || find(c.begin(), c.end(), s[j]) != c.end()) {
            res.push_back(s.substr(i, j - i + 1));
            break;
        }
        if (s[i] != s[j]) {
            res.push_back(s.substr(i, j - i + 1));
            break;
        }
        i++, j--;
    }
    if (res.empty()) {
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }
    return 0;
}

```