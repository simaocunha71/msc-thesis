    string a;
    char b;
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            a+=' ';
        }
        else{
            b=s[i];
            b+=2;
            b+=2;
            a+=b;
        }
    }
    return a;
}
int main(){
    string a;
    scanf("%s",&a);
    printf("%s",encrypt(a).c_str());
    return 0;
}























*/
#include <bits/stdc++.h>
using namespace std;

string encrypt(string s) {
    string result;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            result += ' ';
        } else {
            result += char(s[i] + 2 + 2);
        }
    }
    return result;
}

int main() {
    string s;
    cin >> s;
    cout << encrypt(s) << endl;
    return 0;
}

```