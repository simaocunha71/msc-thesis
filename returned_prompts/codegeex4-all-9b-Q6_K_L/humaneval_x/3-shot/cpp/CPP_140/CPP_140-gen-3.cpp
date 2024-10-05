    string new_text;
    int i;
    int counter=0;
    char chr;
    for (i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr==' ')
        {
            counter+=1;
            if (counter<3)
            {
                new_text+=' ';
            }
            if (counter==3)
            {
                new_text+='-';
            }
        }
        else
        {
            counter=0;
            new_text+=chr;
        }
    }
    return new_text;
}

