    int ans = 0;
    for(int i = 0; i < s.length(); i += 2){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            ans++;
        }
    }
    return ans;
}
int main(){
    string s;
    cin>>s;
    cout<<count_upper(s);
    return 0;
}



*/

#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int count_upper(string s){
    int ans = 0;
    for(int i = 0; i < s.length(); i += 2){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            ans++;
        }
    }
    return ans;
}
int main(){
    string s;
    cin>>s;
    cout<<count_upper(s);
    return 0;
}













































































































































































































































































