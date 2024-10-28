    string str_rev,str_pal,str_suf,str_pre;
    int i,j,l;
    str_pal=str;
    while (!is_palindrome(str_pal))
    {
        str_suf=str_pal.substr(str_pal.length()/2,str_pal.length()/2);
        if (is_palindrome(str_suf))
        {
        str_pre=str_pal.substr(0,str_pal.length()/2);
        str_rev=str_pre.rbegin(),str_pre.rend();
        return str_pal+str_rev.substr(0,str_suf.length());
        }
        str_pal+=str_pal.substr(0,str_pal.length()/2);
    }
    return str;
}


