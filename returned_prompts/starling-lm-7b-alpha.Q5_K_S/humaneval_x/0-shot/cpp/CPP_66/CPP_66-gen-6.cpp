    int sum = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] >= 65 && s[i] <= 90){
            sum += s[i];
        }
    }
    return sum;
}


int main(){
    printf("%d\n",digitSum("abAB"));
    return 0;
}













*/
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    string s;
    cin >> s;
    int ans = 0;
    for(char c: s){
        if(c >= 'A' && c <= 'Z'){
            ans += c;
        }
    }
    cout << ans << '\n';

    return 0;
}

```