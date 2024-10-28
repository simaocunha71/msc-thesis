    string new_str;
    char chr;
    int i;
    for (i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr==' ')
        {
            if (new_str.length()>=2 && new_str[new_str.length()-1]==chr && new_str[new_str.length()-2]==chr)
            {
                new_str+=chr;
            }
            else if (new_str.length()>0)
            {
                new_str+="_";
            }
        }
        else
        {
            new_str+=chr;
        }
    }
    return new_str;
}