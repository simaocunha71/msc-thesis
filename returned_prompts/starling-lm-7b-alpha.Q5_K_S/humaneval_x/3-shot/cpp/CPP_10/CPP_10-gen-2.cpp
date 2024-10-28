    string str_rev;
    int i,j;
    int len;

    len=str.length();
    for (i=0;i<len;i++)
    {
        str_rev+=str[len-i-1];
    }

    for (i=0;i<len;i++)
    {
        str_rev+=str[i];
        for (j=0;j<i;j++)
        {
            if (is_palindrome(str_rev.substr(i,len-2*i)))
            {
                return str_rev.substr(0,i)+str_rev.substr(i,len-2*i)+str_rev.substr(len-i,i);
            }
        }
    }
    return str;
}


