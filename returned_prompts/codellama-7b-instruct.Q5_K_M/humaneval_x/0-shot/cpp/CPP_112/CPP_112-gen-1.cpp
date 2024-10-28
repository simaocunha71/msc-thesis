vector<string> v;
string s1="";
for(int i=0;i<s.size();i++){
    if(!c.find(s[i])){
        continue;
    }
    else{
        s1.push_back(s[i]);
    }
}

reverse(s1.begin(),s1.end());
if(s1==s1){
    v.push_back(s1);
    v.push_back("True");
}
else{
    v.push_back(s1);
    v.push_back("False");
}
return v;
}
int main(){
string s="abcde";
string c="ae";
vector<string> v=reverse_delete(s,c);
cout<<v[0]<<endl;
cout<<v[1]<<endl;
}


Ans:

#include<iostream>
#include<string>
#include<vector>
using namespace std;

vector<string> reverse_delete(string s, string c) {
    vector<string> v;
    string s1 = "";
    for (int i = 0; i < s.size(); i++) {
        if (c.find(s[i]) != string::npos) {
            continue;
        }
        else {
            s1 += s[i];
        }
    }
    reverse(s1.begin(), s1.end());
    if (s1 == s1) {
        v.push_back(s1);
        v.push_back("True");
    }
    else {
        v.push_back(s1);
        v.push_back("False");
    }
    return v;
}

int main() {
    string s = "abcde";
    string c = "ae";
    vector<string> v = reverse_delete(s, c);
    cout << v[0] << endl;
    cout << v[1] << endl;
    return 0;
}
