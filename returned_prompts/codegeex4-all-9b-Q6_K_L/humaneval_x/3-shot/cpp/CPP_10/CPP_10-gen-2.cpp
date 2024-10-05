    string s(str.rbegin(),str.rend());
    if (is_palindrome(str))
    return str;
    else return str+s;
}

