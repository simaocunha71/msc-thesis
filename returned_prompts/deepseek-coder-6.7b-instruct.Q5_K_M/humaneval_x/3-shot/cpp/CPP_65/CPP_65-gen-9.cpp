    string str = to_string(x);
    int len = str.length();

    if (shift >= len)
        return string(str.rbegin(), str.rend());

    rotate(str.begin(), str.begin()+str.length()-shift, str.end());
    return str;
}


