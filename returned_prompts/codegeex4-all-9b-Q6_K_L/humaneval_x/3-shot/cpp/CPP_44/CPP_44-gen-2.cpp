    string result="";
    while (x>0)
    {
        int remainder=x%base;
        result=char(remainder+48)+result;
        x=x/base;
    }
    return result;
}

