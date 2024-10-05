    string str_x=to_string(x);
    string str_shift="";
    int i;
    for (i=1;i<=shift;i++)
    {
        str_shift=str_x[i-1]+str_shift;
    }

    str_x=str_x.substr(0,str_x.length()-shift)+str_shift;
    return str_x;
}

