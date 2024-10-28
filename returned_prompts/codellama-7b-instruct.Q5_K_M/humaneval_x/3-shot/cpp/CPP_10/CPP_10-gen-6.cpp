    if (is_palindrome(str)) return str;

    int i;
    for (i=str.length();i>0;i--)
    if (is_palindrome(str.substr(0,i)))
    {
        string palindrome(str.substr(0,i));
        palindrome+=str.substr(i,str.length()-i);
        return palindrome;
    }
    return "";
}


