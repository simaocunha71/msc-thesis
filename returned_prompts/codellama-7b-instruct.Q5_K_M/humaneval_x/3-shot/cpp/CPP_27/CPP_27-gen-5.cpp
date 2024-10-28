    int i;
    char chr;
    string flipped_str;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (chr>='a' && chr<='z')
        {
            flipped_str+=(chr-32);
        }
        else if (chr>='A' && chr<='Z')
        {
            flipped_str+=(chr+32);
        }
        else
        {
            flipped_str+=chr;
        }
    }
    return flipped_str;
}


