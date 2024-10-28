    int i;
    int j;
    for (i=str.length()-1;i>=0;i--)
    if (is_palindrome(str.substr(0,i+1)))
    {
        for (j=0;j<str.length()-i-1;j++)
        str+=str[j];
        return str;
    }
}



