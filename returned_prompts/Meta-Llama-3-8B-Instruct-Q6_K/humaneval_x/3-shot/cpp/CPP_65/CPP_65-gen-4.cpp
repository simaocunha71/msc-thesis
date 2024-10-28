    string str = to_string(x);
    shift = shift % str.length();
    return str.substr(shift) + str.substr(0, shift);
}