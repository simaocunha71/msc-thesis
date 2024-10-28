    int i;
    string new_text="";
    int count=0;
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            count+=1;
        }
        else
        {
            count=0;
        }
        if (count<3)
        {
            new_text+="_";
        }
        else
        {
            new_text+="-";
        }
        new_text+=" ";
    }
    return new_text;
}



