    for(auto i : c)
        s.erase(remove(s.begin(), s.end(), i), s.end());

    string reversed_s = s;
    reverse(reversed_s.begin(), reversed_s.end());

    bool is_palindrome = s == reversed_s;

    return {s, is_palindrome ? "True" : "False"};
}


