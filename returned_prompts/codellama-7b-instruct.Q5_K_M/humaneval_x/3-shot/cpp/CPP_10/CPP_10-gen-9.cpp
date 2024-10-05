    string palindrome;
    if (is_palindrome(str))
    return str;
    
    int i;
    for (i=str.length()-1;i>=0;i--)
    if (is_palindrome(str.substr(0,i+1)))
    {
    palindrome=str.substr(0,i+1);
    break;
    }
    palindrome+=string(str.rbegin(),str.rend());
    return palindrome;
}


