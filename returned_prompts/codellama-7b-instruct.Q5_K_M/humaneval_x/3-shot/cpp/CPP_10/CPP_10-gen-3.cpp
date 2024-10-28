    int i,j;
    string s;
    for (i=0;i<str.length();i++)
    {
        s=str.substr(0,i+1);
        if (is_palindrome(s))
        {
            s+=str.substr(0,i+1);
            return s;
        }
    }
    return str;
}




