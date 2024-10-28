    vector<string> words;
    int i;
    int j;
    int k;
    char chr;
    for (i=0;i<txt.length();i++)
    {
        chr=txt[i];
        if (chr==' '||chr==','||chr=='\'')
        {
            j=i;
            while (txt[j]==' '||txt[j]==','||txt[j]=='\'')
                j++;
            for (k=j;k<=i;k++)
                words.push_back(txt.substr(k,i-k+1));
            i=j-1;
        }
    }
    if (words.size()==0)
    {
        for (i=0;i<txt.length();i++)
            if (txt[i]>='a'&&txt[i]<='z')
                if ((txt[i]-'a')%2==1)
                    words.push_back("1");
                
        if (words.size()==0)
            words.push_back("0");
    }
    return words;
}



