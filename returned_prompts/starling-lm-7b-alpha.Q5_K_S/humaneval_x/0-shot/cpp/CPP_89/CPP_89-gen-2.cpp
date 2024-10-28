    for(int i=0;i<s.length();i++)
    {
        if(s[i]>='a'&&s[i]<='z')
        {
            s[i]=s[i]+2*2;
        }
        else if(s[i]>='A'&&s[i]<='Z')
        {
            s[i]=s[i]+2*2;
        }
    }
    return s;
}
int main()
{
    string s;
    cin>>s;
    cout<<encrypt(s);
    return 0;
}

*/
#include <bits/stdc++.h>
using namespace std;
string encrypt(string s) {
    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] = (s[i] - 'a' + 2 * 2) % 26 + 'a';
        else if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = (s[i] - 'A' + 2 * 2) % 26 + 'A';
    }
    return s;
}
int main() {
    string s;
    cin >> s;
    cout << encrypt(s) << endl;
    return 0;
}








































































































































































