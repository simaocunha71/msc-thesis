    string new_text;
    for (int i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            if (new_text.length()>0 && new_text[new_text.length()-1]==' ')
            {
                new_text+= '-';
            }
            else if (new_text.length()==0)
            {
                new_text+='_';
            }
            else
            new_text+='_';
        }
        else
        new_text+=text[i];
    }
    return new_text;
}

