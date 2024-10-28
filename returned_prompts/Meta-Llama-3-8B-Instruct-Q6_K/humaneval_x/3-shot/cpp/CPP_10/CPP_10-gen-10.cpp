    string s(str);
    int len=str.length();
    for (int i=len-1;i>=0;i--)
    {
        if (is_palindrome(s.substr(0,i+1)))
        {
            return s+string(s.rbegin(),s.rend()).substr(len-i-1);
        }
    }
    return str;
}
int main()
{
    cout << is_palindrome("madam") << endl;
    cout << make_palindrome("cat") << endl;
    cout << make_palindrome("cata") << endl;
    return 0;
}  //main
int main()
{
    cout << make_palindrome("") << endl;
    return 0;
}  //main
*/



