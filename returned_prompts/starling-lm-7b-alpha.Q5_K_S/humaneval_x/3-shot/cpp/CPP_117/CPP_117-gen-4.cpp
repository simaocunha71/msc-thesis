    vector<string> result;
    char chr;
    char vowels[]={'a','e','i','o','u'};
    int i,j;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ') continue;
        int count=0;
        for (j=0;j<s.length();j++)
        {
            chr=s[j];
            if (chr==' ') continue;
            if (strchr(vowels,tolower(chr))!=NULL) continue;
            count+=1;
            if (count==n)
            {
                string word="";
                for (int k=i;k<=j;k++)
                {
                    chr=s[k];
                    if (chr==' ') continue;
                    word+=chr;
                }
                result.push_back(word);
                break;
            }
        }
    }
    return result;
}


