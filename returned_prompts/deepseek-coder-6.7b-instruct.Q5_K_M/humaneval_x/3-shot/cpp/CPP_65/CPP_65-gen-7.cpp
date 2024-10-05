    string str = to_string(x);
    int len = str.size();
    if (shift >= len)
        return str;
    rotate(str.begin(), str.begin()+len-shift, str.end());
    return str;
}


