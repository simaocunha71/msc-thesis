    string palindrome_suffix;
    string str_prefix;
    int i;
    for (i=str.length();i>0;i--)
    if (is_palindrome(str.substr(0,i)))
    {
        palindrome_suffix=str.substr(i,str.length()-i);
        str_prefix=str.substr(0,i);
        break;
    }
    return str_prefix+palindrome_suffix+string(palindrome_suffix.rbegin(),palindrome_suffix.rend());
}



