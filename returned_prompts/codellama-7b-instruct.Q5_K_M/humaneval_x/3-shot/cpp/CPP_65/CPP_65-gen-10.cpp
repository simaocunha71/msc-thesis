    string x_str = to_string(x);
    int len = x_str.length();
    if (shift>len)
    return reverse(x_str);
    else
    return x_str.substr(shift,len-shift)+x_str.substr(0,shift);
}


