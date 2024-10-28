    string new_string;
    char chr;
    bool space=true;
    for (int i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr==' ')
        {
            if (space)
            {
                new_string+='_';
                space=false;
            }
            else
            {
                new_string+='-';
                space=true;
            }
        }
        else
        {
            new_string+=chr;
            space=true;
        }
    }
    return new_string;
}  // 1
