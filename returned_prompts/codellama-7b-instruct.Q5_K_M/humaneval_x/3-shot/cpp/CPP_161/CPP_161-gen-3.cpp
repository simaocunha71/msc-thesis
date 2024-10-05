    int i;
    char chr;
    string result="";
    bool is_letter=false;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr>='A'&&chr<='Z')
        {
            result+=chr+'a'-'A';
            is_letter=true;
        }
        else if (chr>='a'&&chr<='z')
        {
            result+=chr+'A'-'a';
            is_letter=true;
        }
        else
        {
            result+=chr;
        }
    }
    if (is_letter)
    return result;
    else
    return result;
}


