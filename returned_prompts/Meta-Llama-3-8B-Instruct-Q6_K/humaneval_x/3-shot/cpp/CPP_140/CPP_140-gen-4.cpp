    string new_text="";
    char chr;
    bool space=true;
    for (int i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr!=' ')
        {
            new_text+=chr;
            space=false;
        }
        else
        {
            if (space)
            {
                new_text+='_';
            }
            else
            {
                new_text+='_';
                space=true;
            }
        }
    }
    return new_text;
}   


