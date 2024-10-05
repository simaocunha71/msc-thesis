    string str = to_string(x);
    int len = str.size();
    if(shift >= len)
        reverse(str.begin(), str.end());
    else{
        reverse(str.begin(), str.begin()+len-shift);
        reverse(str.begin()+len-shift, str.end());
        reverse(str.begin(), str.end());
    }
    return str;
}


