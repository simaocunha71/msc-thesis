    int i;
    string fixed_text;
    int consecutive_spaces=0;
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            if (consecutive_spaces==0)
            fixed_text+="_";
            if (consecutive_spaces>0)
            fixed_text+="-";
            consecutive_spaces+=1;
        }
        else
        {
            fixed_text+=text[i];
            consecutive_spaces=0;
        }
    }
    return fixed_text;
}



