    vector<string> ans;
    int i=0;
    while(i<s.size()){
        if(s[i]==' '||s[i]==','){
            string t="";
            for(int j=i;j<s.size();j++){
                if(s[j]==' '||s[j]==','){
                    break;
                }
                t+=s[j];
            }
            ans.push_back(t);
        }
        i++;
    }
    return ans;
}
int main(){
    string s;
    cin>>s;
    vector<string> ans=words_string(s);
    for(auto &a:ans){
        printf("%s ",a.c_str());
    }
    return 0;
}


































*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    // your code goes here
    string s;
    cin>>s;
    vector<string> ans=words_string(s);
    for(auto &a:ans){
        printf("%s ",a.c_str());
    }
    return 0;
}




























































































































































































