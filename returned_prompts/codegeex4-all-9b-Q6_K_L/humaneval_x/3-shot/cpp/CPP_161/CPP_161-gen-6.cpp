    string s2="";
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if ((chr>='a')&&(chr<='z'))
        s2+=(chr-32);
        if ((chr>='A')&&(chr<='Z'))
        s2+=(chr+32);
        if (((chr>='0')&&(chr<='9'))||(chr=='@')||(chr=='#')||(chr=='$'))
        s2+=chr;
    }
    return s2;
}

