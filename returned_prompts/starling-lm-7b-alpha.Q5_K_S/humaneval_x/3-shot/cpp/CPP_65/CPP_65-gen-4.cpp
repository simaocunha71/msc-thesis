    string str=to_string(x);
    string str_res="";
    int i;
    for (i=0;i<str.length();i++)
    {
        if (i+shift>=str.length())
        {
            str_res+=str[i];
        }
        else{
            str_res+=str[i+shift];
        }
    }
    return str_res;
}



