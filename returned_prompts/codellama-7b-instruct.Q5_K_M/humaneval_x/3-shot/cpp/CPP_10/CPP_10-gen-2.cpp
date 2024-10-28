    int i;
    string postfix;
    string prefix;
    string palindrome;
    string str_rev=str;
    reverse(str_rev.begin(),str_rev.end());
    for (i=0;i<str.length();i++)
    {
        if (is_palindrome(str.substr(i)))
        {
        postfix=str.substr(i);
        prefix=str.substr(0,i);
        }
    }
    return postfix+prefix+str_rev;
}


