    string str;
    str=to_string(x);
    if (shift>str.length())
    str=str.substr(str.length()-1,1)+str.substr(0,str.length()-1);
    else
    str=str.substr(shift)+str.substr(0,shift);
    return str;
}

