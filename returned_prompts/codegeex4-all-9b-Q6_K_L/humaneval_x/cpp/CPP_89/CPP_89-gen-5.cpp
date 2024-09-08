#include <bits/stdc++.h>
#include <string>
using namespace std;
string encrypt(string s)
{
    string out;
    for (int i = 0; i < s.length(); i++)
    {
        if (isupper(s[i]))
        {
            out += (s[i] + 16 - 65) % 26 + 65;
        }
        else if (islower(s[i]))
        {
            out += (s[i] + 16 - 97) % 26 + 97;
        }
        else
        {
            out += s[i];
        }
    }
    return out;
}
int main()
{
    string s;
    cin >> s;
    cout << encrypt(s);
    return 0;
}