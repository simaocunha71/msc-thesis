    string s = to_string(x);
    int n = s.length();
    if(shift>=n)
        shift = shift % n;
    string res = s.substr(shift) + s.substr(0,shift);
    return res;
}
