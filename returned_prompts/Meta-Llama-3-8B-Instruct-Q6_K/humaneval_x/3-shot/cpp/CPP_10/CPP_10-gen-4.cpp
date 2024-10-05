    string s=str;
    for (int i=str.length()-1;i>=0;--i)
    {
        if (is_palindrome(s.substr(0,i+1)))
            return s+string(s.rbegin(),s.rend()).substr(i+1);
    }
    return s+string(s.rbegin(),s.rend());
} 