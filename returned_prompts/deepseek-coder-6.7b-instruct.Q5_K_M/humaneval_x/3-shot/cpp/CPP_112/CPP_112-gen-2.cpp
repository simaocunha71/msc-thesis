    for(char ch : c)
    {
        s.erase(remove(s.begin(), s.end(), ch), s.end());
    }
    string reversed_s = string(s.rbegin(), s.rend());
    bool is_palindrome = (s == reversed_s);
    return {s, is_palindrome ? "True" : "False"};
}


