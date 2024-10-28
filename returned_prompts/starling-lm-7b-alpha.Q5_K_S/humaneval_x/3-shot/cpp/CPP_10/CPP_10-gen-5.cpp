    string s=str;
    for (int i=str.length()-1;i>=0;i--)
    if (is_palindrome(str.substr(0,i+1)))
    {
        return str.substr(0,i+1)+s.substr(i+1,s.length())+
        string(str.substr(0,i+1)).rbegin();
    }
}


