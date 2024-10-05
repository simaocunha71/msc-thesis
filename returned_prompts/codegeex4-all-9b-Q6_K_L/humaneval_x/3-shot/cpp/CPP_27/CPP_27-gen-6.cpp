    string flipped;
    int i;
    char chr;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (chr>='a' && chr<='z')
        flipped+=chr-'a'+'A';
        else if (chr>='A' && chr<='Z')
        flipped+=chr-'A'+'a';
        else
        flipped+=chr;
    }
    return flipped;
}

