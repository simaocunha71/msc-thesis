    string s = to_string(x);
    int n = s.size();
    if(shift >= n)
        shift %= n;
    return s.substr(shift) + s.substr(0, shift);
}