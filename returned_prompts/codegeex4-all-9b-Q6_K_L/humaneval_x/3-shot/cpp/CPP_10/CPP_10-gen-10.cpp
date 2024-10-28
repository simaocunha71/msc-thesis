    string s=str;
    for (int i=str.length();i>=0;i--)
    {
        if (is_palindrome(str.substr(0,i)))
        {
            s+=str.substr(i,str.length()-i);
            break;
        }
    }
    return s;
}