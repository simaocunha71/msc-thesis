    for(auto i : c) {
        s.erase(remove(s.begin(), s.end(), i), s.end());
    }
    string rev_s = s;
    reverse(rev_s.begin(), rev_s.end());
    bool is_palindrome = (s == rev_s);
    return {s, is_palindrome ? "True" : "False"};
}


