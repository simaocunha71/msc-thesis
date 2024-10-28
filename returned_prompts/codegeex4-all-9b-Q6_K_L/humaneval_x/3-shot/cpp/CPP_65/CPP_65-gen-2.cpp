    string str=to_string(x);
    int length=str.length();
    if (shift>length)
    {
    string reverse="";
    for (int i=length-1;i>=0;i--)
        reverse+=str[i];
    return reverse;
    }
    string result="";
    for (int i=shift;i<length;i++)
        result+=str[i];
    for (int i=0;i<shift;i++)
        result+=str[i];
    return result;
}

