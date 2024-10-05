    int i,j,k;
    int len=str.length();
    string postfix="", prefix="";
    for (i=0;i<len;i++)
    {
        postfix=str.substr(i,len-i);
        if (is_palindrome(postfix))
        break;
    }
    if (i==len)
    return str;
    for (j=0;j<i;j++)
    {
        prefix=str.substr(0,i-j);
        if (is_palindrome(prefix))
        break;
    }
    string s=prefix+postfix;
    return s;
}


