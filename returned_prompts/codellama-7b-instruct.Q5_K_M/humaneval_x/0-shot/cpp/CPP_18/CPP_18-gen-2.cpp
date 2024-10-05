    if(str.find(substring)==string::npos)
        return 0;
    str.erase(0,str.find(substring)+substring.length());
    goto A;
}

