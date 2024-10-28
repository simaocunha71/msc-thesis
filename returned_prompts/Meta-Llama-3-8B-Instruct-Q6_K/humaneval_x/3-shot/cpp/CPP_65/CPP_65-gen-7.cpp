    string s = to_string(x);
    int len = s.length();
    shift = shift % len;
    if (shift > 0) {
        s = s.substr(shift) + s.substr(0, shift);
    } else {
        s = s.substr(len + shift) + s.substr(0, len + shift);
    }
    return s;
}