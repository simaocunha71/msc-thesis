    string str;
    int shift_left=shift%to_string(x).length();
    int i;
    for (i=0;i<to_string(x).length();i++)
    {
        str+=to_string(x)[(i+shift_left)%to_string(x).length()];
    }
    return str;
}  



