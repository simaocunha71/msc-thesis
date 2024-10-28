    string rev;
    string result;
    int i,j;
    int l=str.length();
    for (i=0;i<l;i++)
    {
        rev="";
        for (j=i;j<l;j++)
        rev+=str[j];
        if (is_palindrome(rev))
        {
        result+=str.substr(0,i+1);
        result+=rev;
        return result;
        }
    }
    return "Can't make palindrome";
}
