    string words[100];
    int i,j;
    char chr;
    int word_count=0;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '){
        word_count+=1;
        }
        else{
            words[word_count]+=chr;
        }
    }

    for (i=0;i<word_count;i++)
    {
        sort(words[i].begin(), words[i].end());
    }

    s="";
    for (i=0;i<word_count;i++)
    {
        s+=words[i];
        s+=" ";
    }

    return s;
}





