    for(int i = 0; i < s.length(); i++){
        if(s[i] >= 'a' && s[i] <= 'z')
            s[i] = s[i] - 'a' + 'A';
        else if(s[i] >= 'A' && s[i] <= 'Z')
            s[i] = s[i] - 'A' + 'a';
    }
    return s;
}
int main(){
    string s;
    cin >> s;
    cout << solve(s) << endl;
    return 0;
}

*/



#include <bits/stdc++.h>
using namespace std;

string solve(string s){
    for(int i = 0; i < s.length(); i++){
        if(s[i] >= 'a' && s[i] <= 'z')
            s[i] = s[i] - 'a' + 'A';
        else if(s[i] >= 'A' && s[i] <= 'Z')
            s[i] = s[i] - 'A' + 'a';
    }
    return s;
}

int main(){
    string s;
    cin >> s;
    cout << solve(s) << endl;
    return 0;
}

```