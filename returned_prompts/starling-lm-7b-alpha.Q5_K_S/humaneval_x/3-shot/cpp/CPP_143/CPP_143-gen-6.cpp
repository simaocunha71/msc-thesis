    int i;
    string res;
    char chr;
    for (i=0;i<sentence.length();i++)
    {
        chr=sentence[i];
        if (chr==' ')
        {
            if (res.length()==2 || res.length()==3 || res.length()==5 || res.length()==7)
            {
                res+=" ";
            }
        }
        else
        {
            res+=chr;
        }
    }
    return res;
}


