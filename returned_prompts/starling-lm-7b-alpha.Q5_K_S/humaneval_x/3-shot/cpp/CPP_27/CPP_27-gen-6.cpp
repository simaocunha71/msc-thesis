    string ret_str="";
    for (char chr:str)
    {
        if (chr>='A' && chr<='Z')
        {
        ret_str+=tolower(chr);
        }
        else if (chr>='a' && chr<='z')
        {
        ret_str+=toupper(chr);
        }
        else ret_str+=chr;
    }
    return ret_str;
}


