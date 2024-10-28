    string new_str;
    for (int i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr>='a' && chr<='z')
        {
            int chr_num=chr-'a';
            chr_num+=4;
            chr_num%=26;
            chr=chr_num+'a';
        }
        new_str+=chr;
    }
    return new_str;
}

