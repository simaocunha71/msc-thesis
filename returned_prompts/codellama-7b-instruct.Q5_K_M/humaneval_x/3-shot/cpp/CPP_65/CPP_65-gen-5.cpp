    string str_x = to_string(x);
    string result;
    int i;
    for (i=shift;i<str_x.length();i++)
    result+=str_x[i];
    for (i=0;i<shift;i++)
    result+=str_x[i];
    return result;
}



