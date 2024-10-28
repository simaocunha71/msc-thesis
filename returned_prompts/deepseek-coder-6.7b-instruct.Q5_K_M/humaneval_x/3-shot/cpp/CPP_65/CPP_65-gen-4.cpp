    string str = to_string(x);
    int length = str.size();
    if(shift >= length)
    {
        reverse(str.begin(), str.end());
        return str;
    }
    else
    {
        rotate(str.begin(), str.begin()+length-shift, str.end());
        return str;
    }
}


