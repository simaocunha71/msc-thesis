    string x_str;
    x_str=to_string(x);
    int length=x_str.length();
    if (shift>length)
    {
        string temp=x_str;
        for (int i=0;i<length;i++)
        {
        x_str[i]=temp[length-i-1];
        }
        return x_str;
    }
    string temp=x_str.substr(0,shift);
    x_str=x_str.substr(shift,x_str.length());
    x_str+=temp;
    return x_str;
}

