    vector<string> words;
    string temp;
    int i;
    for (i=0;i<txt.length();i++)
    {
        char chr=txt[i];
        if (chr==' ')
        {
            words.push_back(temp);
            temp="";
        }
        if (chr==',')
        {
            words.push_back(temp);
            temp="";
        }
        else
        {
            temp+=chr;
        }
    }
    if (temp.length()>0)
    words.push_back(temp);
    else
    {
        int sum=0;
        for (i=0;i<txt.length();i++)
        {
            if (txt[i]>='a' && txt[i]<='z')
                if ((int)txt[i]%2==1)
                    sum+=1;
        }
        temp=to_string(sum);
        words.push_back(temp);
    }
    return words;
}