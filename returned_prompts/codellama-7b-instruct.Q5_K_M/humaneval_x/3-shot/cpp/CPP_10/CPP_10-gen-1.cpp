    if (is_palindrome(str))
    return str;
    int i;
    for (i=0;i<str.length()/2;i++)
    if (str[i]!=str[str.length()-i-1])
    break;

    string suffix=str.substr(i,str.length()-i);
    string prefix=str.substr(0,i);
    return suffix+prefix+suffix;
}


