#include <bits/stdc++.h>
using namespace std;
bool is_palindrome(string text)
{
    int i = 0;
    int j = text.length() - 1;
    while (i < j)
    {
        if (text[i] != text[j])
        {
            return false;
        }
        i++;
        j--;
    }
    return true;
}
int main()
{
    string s = "madam";
    if (is_palindrome(s))
    {
        cout << "yes" << endl;
    }
    else
    {
        cout << "no" << endl;
    }
    return 0;
}
