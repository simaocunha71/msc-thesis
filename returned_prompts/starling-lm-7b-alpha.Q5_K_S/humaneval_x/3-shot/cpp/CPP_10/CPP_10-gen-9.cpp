    string str_rev(str);
    str_rev.erase(str_rev.begin());
    str+=str_rev;
    while (!is_palindrome(str))
    {
        str_rev.erase(str_rev.begin());
        str+=str_rev;
    }
    return str;
}


