    string s = to_string(x);
    int len = s.length();
    if(shift >= len) shift = shift % len;
    string result = s.substr(shift) + s.substr(0, shift);
    return result;
}
