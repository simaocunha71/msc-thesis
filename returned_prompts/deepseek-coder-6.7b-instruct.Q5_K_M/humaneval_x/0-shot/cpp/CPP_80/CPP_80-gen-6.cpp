if (s.size() < 3){
    return false;
}
for (int i = 0; i < s.size() - 2; i++){
    if (s[i] == s[i + 1] || s[i + 1] == s[i + 2] || s[i] == s[i + 2]){
        return false;
    }
}
return true;
}
int main(){
string s;
cin>>s;
cout<<(is_happy(s) ? "true" : "false");
return 0;
}
*/

#include <iostream>
#include <string>
using namespace std;

bool is_happy(string s) {
    if (s.length() < 3) return false;
    for (int i = 0; i < s.length() - 2; i++) {
        if (s[i] == s[i + 1] || s[i + 1] == s[i + 2] || s[i] == s[i + 2])
            return false;
    }
    return true;
}

int main() {
    string s;
    cin >> s;
    cout << (is_happy(s) ? "true" : "false");
    return 0;
}
//Time complexity: O(n)
//Space complexity: O(1)

//Q2:
/*
