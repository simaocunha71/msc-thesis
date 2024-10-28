    string str = to_string(x);
    int n = str.length();
    shift = shift % n;
    if(shift == 0) return str;
    return str.substr(shift) + str.substr(0, shift);
}  // 2
}  // 1
}  // 0


